from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, User
import hashlib

# 创建蓝图
user_bp = Blueprint('user', __name__, url_prefix='/user')

# -------------------------------
# 工具函数：MD5 加密
# -------------------------------
def md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

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

        user = User.query.filter_by(username=username).first()
        if user and user.password == md5(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('登录成功！', 'success')
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
    return render_template('profile.html', user=user)