from flask import Blueprint, render_template

echarts_bp = Blueprint('echarts_page', __name__)

@echarts_bp.route("/echarts")
def echarts():
    return render_template("echarts.html")