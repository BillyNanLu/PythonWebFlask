from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///house.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False