from flask import current_app, request, g

# from App2 import app

def print_config():
    print(f"SECRET_KEY: {current_app.config['SECRET_KEY']}")

# @current_app.before_request
# def check_login():
#     if not request.authorization:
#         g.user = None
#     else:
#         g.user = request.authorization