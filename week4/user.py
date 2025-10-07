from flask import Blueprint

user = Blueprint('user', __name__)  # 创建蓝图


@user.route('/login')  # 定义URL规则
def login():
    return 'user_login'


@user.route('/register')  # 定义URL规则
def register():
    return 'user_register'
