from settings import db

from datetime import datetime


# ======================= 角色表 =======================
class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False, comment='角色名称')
    description = db.Column(db.String(255), comment='角色描述')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f'<Role {self.role_name}>'

    def to_dict(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# ======================= 用户表 =======================
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    gender = db.Column(db.Enum('male', 'female'), default='male')
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False, comment='MD5加密')
    email = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(255), comment='头像图片路径')
    status = db.Column(db.Boolean, default=True, comment='1=active, 0=inactive')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id', ondelete='RESTRICT'), nullable=False, default=3)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    chat_histories = db.relationship('AIChatHistory', backref='user', lazy=True)
    orders = db.relationship('CourseOrder', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "gender": self.gender,
            "phone": self.phone,
            "email": self.email,
            "avatar": self.avatar,
            "status": self.status,
            "role_id": self.role_id,
            "last_login": self.last_login,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# ======================= AI 聊天记录 =======================
class AIChatHistory(db.Model):
    __tablename__ = 'ai_chat_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<AIChatHistory user_id={self.user_id} role={self.role}>'

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "role": self.role,
            "message": self.message,
            "timestamp": self.timestamp
        }


# ======================= 预约咨询表 =======================
class AppointConsult(db.Model):
    __tablename__ = 'appoint_consult'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<AppointConsult {self.appointment_id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "appointment_id": self.appointment_id,
            "name": self.name,
            "phone": self.phone,
            "description": self.description,
            "created_at": self.created_at
        }


# ======================= 职业规划咨询预约信息表 =======================
class AppointInformation(db.Model):
    __tablename__ = 'appoint_information'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.String(20), nullable=False)
    paid_consult = db.Column(db.Enum('yes', 'no'), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.SmallInteger, default=0, comment='0=待处理, 1=已处理, 2=已取消')

    def __repr__(self):
        return f'<AppointInformation {self.appointment_id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "appointment_id": self.appointment_id,
            "name": self.name,
            "phone": self.phone,
            "time": self.time,
            "city": self.city,
            "industry": self.industry,
            "experience": self.experience,
            "paid_consult": self.paid_consult,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# ======================= 课程分类 =======================
class CourseCategory(db.Model):
    __tablename__ = 'course_category'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, default=0)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20))

    courses = db.relationship('Course', backref='category', lazy=True)

    def __repr__(self):
        return f'<CourseCategory {self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "parent_id": self.parent_id,
            "name": self.name,
            "type": self.type
        }


# ======================= 课程表 =======================
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('course_category.id'))
    name = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.String(255))
    intro = db.Column(db.Text)
    target_user = db.Column(db.Text)
    recommendation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    more_info = db.relationship('CourseMore', backref='course', lazy=True)
    orders = db.relationship('CourseOrder', backref='course', lazy=True)
    teachers = db.relationship('Teacher', secondary='course_teacher', backref=db.backref('courses', lazy='dynamic'))

    def __repr__(self):
        return f'<Course {self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "name": self.name,
            "tags": self.tags,
            "intro": self.intro,
            "target_user": self.target_user,
            "recommendation": self.recommendation,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# ======================= 课程附加信息 =======================
class CourseMore(db.Model):
    __tablename__ = 'course_more'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    image = db.Column(db.String(255), comment='图片')
    price = db.Column(db.Numeric(10, 2), comment='原价')
    discount = db.Column(db.Numeric(5, 2), comment='折扣')

    def __repr__(self):
        return f'<CourseMore course_id={self.course_id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "image": self.image,
            "price": float(self.price) if self.price else None,
            "discount": float(self.discount) if self.discount else None
        }


# ======================= 课程订单 =======================
class CourseOrder(db.Model):
    __tablename__ = 'course_order'

    id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(30), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    pay_method = db.Column(db.String(20), default='未选择')
    status = db.Column(db.String(20), default='未支付')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<CourseOrder {self.order_no}>'

    def to_dict(self):
        return {
            "id": self.id,
            "order_no": self.order_no,
            "course_id": self.course_id,
            "user_id": self.user_id,
            "pay_method": self.pay_method,
            "status": self.status,
            "created_at": self.created_at,
            "paid_at": self.paid_at
        }


# ======================= 教师表 =======================
class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50))
    department = db.Column(db.String(50))
    expertise = db.Column(db.Text)
    profile = db.Column(db.Text)
    imgage = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Teacher {self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "department": self.department,
            "expertise": self.expertise,
            "profile": self.profile,
            "imgage": self.imgage,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# ======================= 课程-教师关联表 =======================
class CourseTeacher(db.Model):
    __tablename__ = 'course_teacher'

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), primary_key=True)

    def __repr__(self):
        return f'<CourseTeacher course={self.course_id} teacher={self.teacher_id}>'

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "teacher_id": self.teacher_id
        }
