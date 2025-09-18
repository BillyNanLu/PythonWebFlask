from flask import Flask, after_this_request

app = Flask(__name__)

def index_new():
    print("Index new")
    return "<h1>Index new</h1>"
app.add_url_rule('/index', view_func=index_new)


@app.route('/hello')
@app.route('/hello1')
def hello_flask1():
    return "<p>Hello, Flask!</p>"


@app.route('/hello2/<int:page>', methods=['GET', 'POST'])
def hello_flask2(page):
    return f"<p>current page is {page}!</p>"


@app.get('/hello3/<int:page>')
def hello_flask3(page):
    print('hello_flask3', page)

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




if __name__ == '__main__':
    app.run(debug=True, port=5000)