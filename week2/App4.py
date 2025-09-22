from flask import Flask, render_template, flash, redirect, session, request, url_for

app = Flask(__name__,template_folder='templates')

"""
模版与模版引擎Jinjia2
"""

@app.route('/index')
def index():
    return render_template("index.html", name="name")

@app.route('/filters')
def use_of_filters():
    num = -2.3
    li = [2, 1, 5, 6, 7, 4, 4]
    string = "flask"
    return render_template("filters.html", num=num, li=li, string=string)

"""
选择结构
"""
@app.route('/query-score/<int:score>')
def query_score(score):
    return render_template('select_score.html', score=score)


"""
iKun案例
"""
@app.route('/iKun')
def iKun():
    title = "iKun"
    data = {
        "username": "练习生蔡徐坤 ",
        "img_url": "https://p0.itc.cn/images01/20230207/952e7bde938345f18617bb4ca5ee2b50.png",
        "hobbies": ["唱跳", "篮球", "rap"],
    }
    return render_template(
        "ikun.html",
        title=title,
        **data,
        # img_url=data["img_url"],
        # username=data["username"],
        # hobbies=data["hobbies"],
    )  # ** data 表示将字典拆分为键值对参数


if __name__ == '__main__':
    app.run(debug=True, port=5000)