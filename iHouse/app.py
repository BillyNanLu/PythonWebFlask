from flask import Flask, render_template, request
from settings import Config, db
from index import index_page
from list import list_page
from detail import detail_page
from echarts_page import echarts_bp

app = Flask(__name__)
config = Config()
app.config.from_object(config)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(list_page, url_prefix="/")
app.register_blueprint(detail_page, url_prefix="/")
app.register_blueprint(echarts_bp, url_prefix="/")


if __name__ == "__main__":
    app.run()