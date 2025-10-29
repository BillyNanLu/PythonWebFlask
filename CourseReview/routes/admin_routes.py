from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from models import db, User, Course, Review
from sqlalchemy import func
from sqlalchemy import desc


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# 管理员登录验证装饰器
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' not in session or session['role'] != 1:
            flash('请先使用管理员账号登录', 'error')
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/')
@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    user_count = User.query.count()
    course_count = Course.query.count()
    review_count = Review.query.count()

    # 🔹 联合查询最新 5 条评论
    latest_reviews = (
        db.session.query(
            Review.id,
            Review.comment,
            Review.rating,
            Review.create_time,
            User.username.label('user_name'),
            Course.name.label('course_name')
        )
        .join(User, User.id == Review.user_id)
        .join(Course, Course.id == Review.course_id)
        .order_by(desc(Review.create_time))
        .limit(5)
        .all()
    )

    # 📊 获取课程评论数
    course_review_data = db.session.query(
        Course.name, func.count(Review.id)
    ).outerjoin(Review, Review.course_id == Course.id) \
        .group_by(Course.name).all()

    # 📊 获取评分分布
    rating_query = db.session.query(
        Review.rating, func.count(Review.id)
    ).group_by(Review.rating).all()

    # 转换格式：[{name: '1星', value: 数量}, {name: '2星', value: 数量}, ...]
    rating_data = [
        {"name": f"{rating} 星", "value": count}
        for rating, count in rating_query
    ]

    return render_template(
        'admin/dashboard.html',
        user_count=user_count,
        course_count=course_count,
        review_count=review_count,
        latest_reviews=latest_reviews,
        course_review_data=course_review_data,
        rating_data=rating_data
    )



@admin_bp.route('/users')
@admin_required
def users():
    users = User.query.order_by(User.create_time.asc()).all()
    return render_template('admin/users.html', users=users)

# 删除用户
@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    # 不允许管理员删除自己
    if user.id == session.get('user_id'):
        flash('不能删除自己！', 'error')
        return redirect(url_for('admin.users'))

    db.session.delete(user)
    db.session.commit()
    flash('用户已删除', 'success')
    return redirect(url_for('admin.users'))


# 切换用户角色（普通用户 <-> 管理员）
@admin_bp.route('/users/toggle_role/<int:user_id>', methods=['POST'])
@admin_required
def toggle_user_role(user_id):
    user = User.query.get_or_404(user_id)

    # 不允许管理员修改自己的权限
    if user.id == session.get('user_id'):
        flash('不能修改自己的角色！', 'error')
        return redirect(url_for('admin.users'))

    user.role = 0 if user.role == 1 else 1
    db.session.commit()
    flash('用户角色已更新', 'success')
    return redirect(url_for('admin.users'))



# 课程管理列表
@admin_bp.route('/courses')
@admin_required
def courses():
    all_courses = Course.query.order_by(Course.create_time.desc()).all()
    return render_template('admin/courses.html', courses=all_courses)

# 新增课程
@admin_bp.route('/courses/add', methods=['GET', 'POST'])
@admin_required
def add_course():
    if request.method == 'POST':
        name = request.form.get('name')
        teacher = request.form.get('teacher')
        description = request.form.get('description')

        if not name:
            flash('课程名称不能为空', 'error')
            return redirect(url_for('admin.add_course'))

        new_course = Course(name=name, teacher=teacher, description=description)
        db.session.add(new_course)
        db.session.commit()
        flash('课程新增成功', 'success')
        return redirect(url_for('admin.courses'))

    return render_template('admin/add_course.html')

# 删除课程
@admin_bp.route('/courses/delete/<int:course_id>', methods=['POST'])
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('课程已删除', 'success')
    return redirect(url_for('admin.courses'))

# 编辑课程
@admin_bp.route('/courses/edit/<int:course_id>', methods=['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)

    if request.method == 'POST':
        name = request.form.get('name')
        teacher = request.form.get('teacher')
        description = request.form.get('description')

        if not name:
            flash('课程名称不能为空', 'error')
            return redirect(url_for('admin.edit_course', course_id=course.id))

        course.name = name
        course.teacher = teacher
        course.description = description
        db.session.commit()
        flash('课程信息已更新', 'success')
        return redirect(url_for('admin.courses'))

    return render_template('admin/edit_course.html', course=course)



# 查看所有课程评论
@admin_bp.route('/comments')
@admin_required
def comments():
    comments = Review.query.order_by(Review.create_time.asc()).all()
    return render_template('admin/comments.html', comments=comments)


# 删除评论
@admin_bp.route('/comments/delete/<int:comment_id>', methods=['POST'])
@admin_required
def delete_comment(comment_id):
    comment = Review.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('评论已删除', 'success')
    return redirect(url_for('admin.comments'))