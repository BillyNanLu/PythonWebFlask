from flask import Flask, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "Your secret key&^52@!"
# app.config["SESSION_COOKIE_NAME"] = "my_session"  # 修改 session cookie 名称

# 判断用了chrome还是edge浏览器访问页面
@app.route("/index")
def index():
    user_agent = request.user_agent.string.lower()
    print(f"User-Agent: {user_agent}")
    if "edg" in user_agent:
        user_agent = "Edge"
    elif "chrome" in user_agent:
        user_agent = "Chrome"
    return f"User-Agent: {user_agent}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return "登录成功"

    return """
            <form method="post">
            <p><input type=text name=username placeholder="输入用户名">
            <p><input type=submit value='登录'>
            </form>
            """

@app.route("/home")
def home():
    if "username" in session:
        username = session["username"]
        return f"hello, {username}, this is home page"
    return "请登录"



if __name__ == "__main__":
    app.run(debug=True, port=5000)