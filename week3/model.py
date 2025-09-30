from App7 import db, app

class User (db.Model):
    # __tablename__ = "users"  # 可以修改表名字
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f"User: {self.username}, email: {self.email}"

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()