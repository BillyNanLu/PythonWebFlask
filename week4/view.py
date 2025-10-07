from flask.views import View
# 定义视图类
class MyView(View):
    def dispatch_request(self):  # 重写dispatch_request()方法
        return 'Hello, Flask'