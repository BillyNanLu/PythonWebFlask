from flask import Blueprint

admin = Blueprint("admin", __name__)  # 创建蓝图


@admin.route("/login")  # 定义URL规则
def login():
    return "admin_login"


@admin.route("/add")
def add():
    return "admin_add"
