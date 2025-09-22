from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    name = "Billy"
    return render_template("index.html", name=name)


# 内置过滤器
@app.route("/filters")
def use_of_filters():
    num = -2.3
    li = [2,1, 5, 6, 7, 4, 4]
    string = "flask"
    return render_template("filters.html", num=num, string=string)


@app.router("/score/<int:score>")
def query_score(score):
    return render_template("select_struct.html", score=score)


@app.route("/ikun")
def ikun():
    return render_template("ikun.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)