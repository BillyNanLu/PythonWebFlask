from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, User, Review, Course
import hashlib
from urllib.parse import urlparse, urljoin

# 创建蓝图
user_bp = Blueprint('user', __name__, url_prefix='/user')

# -------------------------------
# 工具函数：MD5 加密
# -------------------------------
def md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# -------------------------------
# 工具函数：安全跳转判断
# -------------------------------
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# -------------------------------
# 注册页面 + 提交注册
# -------------------------------
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('用户名和密码不能为空', 'error')
            return redirect(url_for('user.register'))

        # 检查是否重复注册
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('用户名已存在', 'error')
            return redirect(url_for('user.register'))

        # 创建用户
        new_user = User(username=username, password=md5(password), role=0)
        db.session.add(new_user)
        db.session.commit()

        flash('注册成功，请登录！', 'success')
        return redirect(url_for('user.login'))

    return render_template('register.html')

# -------------------------------
# 登录页面 + 提交登录
# -------------------------------
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        next_page = request.args.get('next')

        user = User.query.filter_by(username=username).first()
        if user and user.password == md5(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('登录成功！', 'success')

            # 管理员跳后台，普通用户跳个人中心
            if user.role == 1:
                return redirect(url_for('admin.dashboard'))
            else:
                # 若存在安全的 next_page 参数（如登录前的受保护页）
                if next_page and is_safe_url(next_page):
                    return redirect(next_page)
                return redirect(url_for('user.profile'))

        else:
            flash('用户名或密码错误', 'error')
            return redirect(url_for('user.login'))

    return render_template('login.html')

# -------------------------------
# 退出登录
# -------------------------------
@user_bp.route('/logout')
def logout():
    session.clear()
    flash('您已退出登录', 'info')
    return redirect(url_for('user.login'))

# -------------------------------
# 个人中心
# -------------------------------
@user_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('请先登录', 'warning')
        return redirect(url_for('user.login'))

    user = User.query.get(user_id)

    # reviews = (
    #     Review.query
    #     .filter_by(user_id=user_id)
    #     .join(Course, Review.course_id == Course.id)
    #     .add_columns(Course.name.label('course_name'), Review.rating, Review.comment, Review.create_time)
    #     .order_by(Review.create_time.desc())
    #     .all()
    # )
    # return render_template('profile.html', user=user, reviews=reviews)
    # ORM 查询 + 联表拿到课程名
    reviews = (
        db.session.query(Review, Course.name.label('course_name'))
        .join(Course, Review.course_id == Course.id)
        .filter(Review.user_id == user_id)
        .order_by(Review.create_time.desc())
        .all()
    )

    # 把查询结果统一封装成字典，方便模板使用
    review_list = [
        {
            'id': r.Review.id,
            'course_name': r.course_name,
            'rating': r.Review.rating,
            'comment': r.Review.comment,
            'create_time': r.Review.create_time
        }
        for r in reviews
    ]

    return render_template('profile.html', user=user, reviews=review_list)

# -------------------------------
# 修改密码
# -------------------------------
@user_bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    user_id = session.get('user_id')
    if not user_id:
        flash('请先登录', 'warning')
        return redirect(url_for('user.login'))

    user = User.query.get(user_id)

    if request.method == 'POST':
        old_pwd = request.form.get('old_password')
        new_pwd = request.form.get('new_password')
        confirm_pwd = request.form.get('confirm_password')

        if not all([old_pwd, new_pwd, confirm_pwd]):
            flash('请填写完整信息', 'error')
            return redirect(url_for('user.change_password'))

        if md5(old_pwd) != user.password:
            flash('原密码错误', 'error')
            return redirect(url_for('user.change_password'))

        if new_pwd != confirm_pwd:
            flash('两次输入的新密码不一致', 'error')
            return redirect(url_for('user.change_password'))

        user.password = md5(new_pwd)
        db.session.commit()

        flash('密码修改成功，请重新登录', 'success')
        session.clear()
        return redirect(url_for('user.login'))

    return render_template('change_password.html', user=user)