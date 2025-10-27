from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from sqlalchemy import func
from models import db, Course, Review

course_bp = Blueprint('course', __name__, url_prefix='/courses')


# 课程列表
@course_bp.route('/')
def list_courses():
    keyword = request.args.get('keyword', '')
    if keyword:
        courses = Course.query.filter(Course.name.like(f"%{keyword}%")).all()
    else:
        courses = Course.query.all()

    avg_ratings = {}
    for c in courses:
        avg = db.session.query(func.avg(Review.rating))\
                .filter(Review.course_id == c.id).scalar()
        avg_ratings[c.id] = round(avg, 1) if avg else 0

    return render_template('courses.html', courses=courses, keyword=keyword, avg_ratings=avg_ratings)

# 课程详情 + 评价展示
@course_bp.route('/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    reviews = Review.query.filter_by(course_id=course_id).order_by(Review.create_time.desc()).all()

    # 计算平均评分
    avg_rating = db.session.query(func.avg(Review.rating)) \
        .filter(Review.course_id == course_id).scalar()
    if avg_rating:
        avg_rating = round(avg_rating, 1)  # 保留一位小数
    else:
        avg_rating = 0

    return render_template('course_detail.html', course=course, reviews=reviews, avg_rating=avg_rating)


# 提交课程评价
@course_bp.route('/<int:course_id>/review', methods=['POST'])
def add_review(course_id):
    if 'user_id' not in session:
        flash('请先登录后再评价！', 'error')
        return redirect(url_for('user.login', next=request.url))

    rating = int(request.form.get('rating'))
    comment = request.form.get('comment')

    # 检查重复评价
    existing = Review.query.filter_by(user_id=session['user_id'], course_id=course_id).first()
    if existing:
        flash('您已评价过该课程！', 'warning')
        return redirect(url_for('course.course_detail', course_id=course_id))

    review = Review(user_id=session['user_id'], course_id=course_id,
                    rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    flash('评价提交成功！', 'success')
    return redirect(url_for('course.course_detail', course_id=course_id))


# 删除自己的评论
@course_bp.route('/delete/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    user_id = session.get('user_id')
    if not user_id:
        flash('请先登录', 'warning')
        return redirect(url_for('user.login'))

    review = Review.query.get_or_404(review_id)

    # 权限判断
    if review.user_id != user_id:
        flash('你无权删除这条评论', 'error')
        return redirect(url_for('course.course_detail', course_id=review.course_id))

    db.session.delete(review)
    db.session.commit()
    flash('评论已删除', 'success')
    return redirect(url_for('course.course_detail', course_id=review.course_id))