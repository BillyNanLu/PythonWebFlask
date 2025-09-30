from flask import Flask, render_template, flash, redirect, session, request, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3, os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///"
    + os.path.join(app.root_path, "database.db")
)
# 动态追踪数据库的修改，不建议开启
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/init_db')
def init_db():
    from model import User

    # 创建User类的对象
    user1 = User(username="小明", email="123@qq.com")
    user2 = User(username="小张", email="456@qq.com")
    user3 = User(username="小红", email="789@qq.com")

    db.session.add(user1)
    db.session.add_all([user2, user3])
    # 将User类的对象添加到数据库会话中
    db.session.commit()
    return "OK"


@app.route('/update/<user_id>')
def update(user_id):
    from model import User
    user = db.session.query(User).get(user_id)
    # 将username的值改为“小兰”
    user.username = "小兰"
    db.session.commit()
    return "OK"


@app.route('/delete/<user_id>')
def delete(user_id):
    # Import User inside the function to avoid circular import
    from model import User
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()
    return "OK"


@app.route('/user/<user_id>')
def get_user(user_id):
    from model import User

    user = db.session.query(User).get(user_id)
    print(user)
    return f"user: {user.username}"


# @app.route("/users")
# def users():
#     from model import User
#
#     # 查询全部记录
#     users = db.session.query(User).all()
#     print(type(users))
#     for u in users:
#         print(u)
#     # 查询第一条记录
#     first_user = db.session.query(User).first()
#     print(first_user)
#     # 查询id >1 的记录
#     users2 = db.session.query(User).filter(User.user_id > 1).all()
#     return f"First user: {users2[1].username} "


@app.route('/user/<user_name>')
def get_user(user_name):
    from model import User

    user = db.session.query(User).filter(User.user_id < 4).all()

    for u in user:
        print(user)
    return f"user: {user[0].email}"


if __name__ == "__main__":
    app.run(debug=True, port=5001)