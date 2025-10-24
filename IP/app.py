from flask import Flask, send_from_directory, render_template
from datetime import datetime
import os

from settings import Config, db
from models import User
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# --------------------------
# 核心：注册 /uploads/ 路径的静态资源路由
# --------------------------
# 1. 获取项目根目录的绝对路径（确保跨环境兼容）
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 2. 定义 /uploads/<path:filename> 路由：匹配所有以 /uploads/ 开头的请求
@app.route('/uploads/<path:filename>')
def serve_uploads(filename):
    # 映射 URL 中的 /uploads/xxx 到本地的 uploads/ 文件夹
    # 例如：/uploads/avatars/xxx.jpg → 本地 uploads/avatars/xxx.jpg
    return send_from_directory(
        directory=os.path.join(BASE_DIR, 'uploads'),  # 本地文件夹路径（项目根目录下的 uploads）
        path=filename,                                # URL 中 /uploads/ 后面的路径（如 avatars/xxx.jpg）
        as_attachment=False                           # False=直接在浏览器显示图片，True=触发下载（按需调整）
    )

# 定义上下文处理器，全局注入now变量
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/home')
def home():
    # 这里需要传递模板中用到的变量，如plannerCourses、departmentTeachers、login_user等
    # 若暂时没有实际数据，可先传递空列表或模拟数据
    return render_template('home.html',
                           plannerCourses=[],
                           departmentTeachers=[],
                           login_user=None)

@app.route('/consult')
def consult():
    return render_template('consult.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# @app.route('/person_center')
# def person_center():
#     return render_template('person_center.html')

# 定义定义一个模拟的用户类
class MockUser:
    def __init__(self):
        self.username = "张小明"  # 用户名
        self.role_id = 2  # 2表示职场塌用户（1管理员，3学生）
        self.avatar = None  # 暂无头像，使用默认图
        self.email = "zhangxiaoming@example.com"  # 邮箱
        self.phone = "13812345678"  # 手机号
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # 注册时间
        self.last_login = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # 最后登录时间

# 定义模拟的课程数据（用于已报名课程列表）
mock_enrolled_courses = [
    {
        "courseId": 1,
        "courseName": "职业生涯规划-基石班",
        "coverImage": "https://picsum.photos/seed/course1/600/400",  # 课程封面
        "categoryName": "职业规划",
        "status": "已支付",
        "paidAt": datetime.now(),
        "payMethod": "微信支付",
        "orderNo": "ORD20231024001"
    },
    {
        "courseId": 2,
        "courseName": "超级个体IP营",
        "coverImage": "https://picsum.photos/seed/course2/600/400",
        "categoryName": "个人成长",
        "status": "已支付",
        "paidAt": datetime.now(),
        "payMethod": "支付宝",
        "orderNo": "ORD20231024002"
    }
]

@app.route('/person_center')
def person_center():
    # 传递模拟数据到模板
    return render_template(
        'person_center.html',
        loginUser=MockUser(),  # 模拟用户对象
        courseCount=2,         # 已报名课程数（和下面列表长度一致）
        careerCount=2,         # 职业规划预约数
        consultCount=1,        # 咨询申请数
        chatCount=5,           # 聊天记录数
        progress=35,           # 学习进度百分比
        enrolledCourses=mock_enrolled_courses  # 已报名课程列表
    )

@app.route('/courseDetail/<int:id>')  # 使用 <变量类型:变量名> 定义路径参数
def courseDetail(id):  # 函数需要接收这个参数
    # 可以在这里根据 id 查询课程详情，比如从数据库获取数据
    # course = 数据库查询逻辑(id)
    return render_template('courseDetail.html', course_id=id)  # 传递给模板

@app.route('/editAccount')
def editAccount():
    return render_template('editAccount.html')

@app.route('/')
def test():
    first_user = User.query.first()
    print(first_user)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)