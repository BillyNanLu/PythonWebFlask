from flask import Flask, send_from_directory
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


@app.route('/')
def test():
    first_user = User.query.first()
    print(first_user)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)