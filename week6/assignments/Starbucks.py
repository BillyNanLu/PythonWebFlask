from flask import Flask, render_template, flash, redirect, session, request, url_for

app = Flask(__name__,template_folder='templates')

@app.route('/starbucks')
def starbucks():
    store_info = {
        "store_no": "55523",
        "store_name": "临港港城新天地店"
    }
    order = {
        "order_number" : "7111",
        "product_price": 24.90,
        "discount_price": 1.00,
        "DP_method": "Meituan",
        "DP_code": "770******927",
        "product_name" : ["星巴克经典咖啡混选中杯单杯MTDP", ""],
        "product_details": ["中/冰/焦糖玛奇朵", "1"],
        "discount_details": ["DCT_1o1_MT activation", ""],
        "order_time": "2025-05-29 11:26:23",
        "invoice_code": "212841aa2204eb39b6d20"
    }
    payment = {
        "payment_method": "Alipay",
        "payment_code": "015******035",
        "payment_money": 3.00,
        "payment_discount": ["支付宝优惠", "¥0.03"]
    }

    return render_template(
        "Starbucks.html",
        **store_info,
        **order,
        **payment
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)