from sqlalchemy.orm.strategy_options import lazyload
from App8 import db, app

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    depart_id = db.Column(db.Integer, db.ForeignKey("department.id"))

    identity = db.relationship("IdentityCard", backref="user", uselist=False)


# 一对一关系
class IdentityCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(18), unique=True, nullable=False)
    # 创建外键
    person_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id", onupdate="CASCADE")
    )  # table name is users not user
    # 定义关系属性，并以标量的形式加载记录


# 一对多关系
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    user = db.relationship("User", backref="departments", uselist=True)

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()