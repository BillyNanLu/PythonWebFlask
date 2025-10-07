from flask import Flask

from user import user
from admin import admin

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# 将蓝图注册到app中
with app.app_context():
    db.create_all()
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(admin, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)
