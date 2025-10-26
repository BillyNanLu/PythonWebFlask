from settings import db

from datetime import datetime

# ---------------------------
# 用户表
# ---------------------------
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.Integer, default=0)  # 0=普通用户，1=管理员
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship('Review', back_populates='user', cascade='all, delete')

    def __repr__(self):
        return f'<User {self.username}>'


# ---------------------------
# 课程表
# ---------------------------
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(50))
    description = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship('Review', back_populates='course', cascade='all, delete')

    def __repr__(self):
        return f'<Course {self.name}>'


# ---------------------------
# 评价表
# ---------------------------
class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='reviews')
    course = db.relationship('Course', back_populates='reviews')

    def __repr__(self):
        return f'<Review {self.id} - User {self.user_id} - Course {self.course_id}>'