# 盛放所有的配置信息
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

# 创建flask-sqlalchemy的实例对象
db = SQLAlchemy()


class Config:
    # 开启调试模式
    DEBUG = False
    # 数据库的类型://用户名:密码@数据库的地址:端口号/数据库的名字
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lunan998998@127.0.0.1:3306/course_review'
    # 压制警告信息
    SQLALCHEMY_TRACK_MODIFICATIONS = True