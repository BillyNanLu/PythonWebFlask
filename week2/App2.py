from flask import Flask, request, session, url_for, current_app, g, redirect
from datetime import timedelta
from util import print_config

app = Flask(__name__)
app1 = Flask(__name__)


# 设置 secret key 的值
# app.secret_key = "Your secret key&^52@!"
app.secret_key = "Your_seccret_key&^52@!"
app1.config["SECRET_KEY"] = "232434"

app.config["SESSION_COOKIE_NAME"] = "my_session"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=5)


# 在脚本中手动激活应用上下文
with app.app_context():
    # 此时可以安全使用 current_app
    print_config()



@app.route("/home")
def home():
    # 用session判断是否登录
    # if "username" in session:
    #     username = session["username"]
    # return f" hello,{g.user}, this is home page."
    return f" hello,{session['username']}, this is home page."

@app.before_request
def check_login():
    if "username" in session:
        g.user = session["username"]
    elif request.endpoint != "login":
        return "未登录", 401

@app.route("/login", methods=["GET", "POST"])
def login():
    # 用session判断是否登录
    if request.method == "POST":
        session["username"] = request.form["username"]  # 设置 session 值
        # session["username"] = request.get_data("username")  # 设置 session 值
        session.permanent = True  # 设置 session 永久有效 (30天)
        return "登录成功! 现在你可以关闭浏览器，再重新打开访问 /home 页面，session应该还在。"

    return """
        <form method="post">
        <p><input type=text name=username placeholder="输入用户名">
        <p><input type=submit value='登录'>
        </form>
        """

@app.route("/logout")
def logout():
    session.clear()  # 清除所有session数据
    return "已退出登录!"



@app.route("/show_config")
@app1.route("/show_config")
def show_config():
    # print_config()
    config = current_app.config["SECRET_KEY"]
    return config
    # return "config printed to console"


# g对象用于在请求期间存储和共享数据
@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    result = a + b  # This sets g.result
    g.result = result
    return f"计算结果: {a} + {b} = {result}"

# g只在同一个request中有效，所以这里g.result是没有值的
@app.route("/get_result")
def get_result():
    return f"计算结果是: {g.result}"



# 书p033例子
@app.route("/")
def get_user():
    g.user_id = "001"  # 将用户id保存到g对象中
    g.user_name = "flask"  # 将用户名称保存到g对象中
    result = db_query()
    return f"{result}"

def db_query():
    user_id = g.user_id  # 使用g对象获取用户id
    user_name = g.user_name  # 使用g对象获取用户名称
    return f"{user_id}:{user_name}"



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # app1.run(debug=True, port=5001)