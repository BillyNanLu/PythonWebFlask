from flask import Flask, after_this_request
app = Flask(__name__)

@app.get('/hello/<int:page>')
def hello_flask(page):
    print('hello_flask', page)

    @after_this_request
    def log_status(response):
        print(response.status_code)
        return response

    return f"<p>current page is {page}!</p>"

@app.before_request
def before_request():
    print("before request")

@app.after_request
def after_request(response):
    print("after request")
    return response

@app.teardown_request
def teardown_request(exception):
    print("teardown request")
    return exception
