import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(app.root_path, "database.db")
    # 这里使用SQLite数据库，数据库文件会自动创建在根目录下
)

# 动态追踪数据库的修改，不建议开启
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/init_db")
def init_db():
    from model2 import User, IdentityCard, Department

    user1 = User(username="xiaoming", email="123@qq.com", depart_id="1")
    user2 = User(username="xiaozhang", email="456@qq.com", depart_id="1")
    user3 = User(username="xiaohong", email="789@qq.com", depart_id="2")

    dept1 =Department(name="Software")
    dept2 =Department(name="Network")

    id_card1 = IdentityCard(number="123456789012345678", person_id=1)
    id_card2 = IdentityCard(number="123456789012345679", person_id=2)
    id_card3 = IdentityCard(number="123456789012345670", person_id=3)

    db.session.add(user1)
    db.session.add([user2, user3])

    db.session.add_all([id_card1, id_card2, id_card3])
    db.session.add_all([dept1, dept2])

    db.session.commit()
    return "OK"


@app.route("/id_number/<user_id>")
def id_number(user_id):
    from model2 import User, IdentityCard
    id_card = db.session.query(IdentityCard).join(User).get(user_id).first()
    # print(id_card)
    # print(type(id_card))

    return f"ID NUMBER: {id_card.number}"


# 查询部门里面有谁
@app.route("/dept/<dept_id>")
def dept_id(dept_id):
    from model2 import Department

    dept = db.session.query(Department).get(dept_id)
    print(dept)
    if dept:
        return f"Department: {dept.name}, has members: {', '.join([u.username for u in dept.user])} "
    else:
        return "Department not found"



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5000)