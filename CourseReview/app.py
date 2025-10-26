from flask import Flask, render_template
from settings import Config, db
from routes.user_routes import user_bp
from routes.course_routes import course_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'lunannanlu'
db.init_app(app)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(course_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)