from flask import Flask, render_template, flash, redirect, session, request, url_for

app = Flask(__name__)

"""
3.6	模板继承
"""


@app.route("/child")
def extends_template():
    # return render_template('base.html')
    return render_template("child.html")


if __name__ == "__main__":
    app.run(debug=True)