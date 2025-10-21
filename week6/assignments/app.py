from flask import Flask, render_template, request
from settings import Config, db
# 导入模型
from models import User, Store, Product, Order, OrderItem, Dp, Payment
from datetime import datetime

app = Flask(__name__)
config = Config()
app.config.from_object(config)
db.init_app(app)


# 路由：/order/<order_id> 显示单个订单详情
@app.route('/order/<int:order_id>')
def show_order(order_id):
    # 查询订单信息
    order = Order.query.get_or_404(order_id)
    # 查询关联的商店信息
    store = Store.query.get(order.store_id)
    # 查询订单项
    order_items = OrderItem.query.filter_by(order_id=order_id).all()
    # 查询DP信息
    dp = Dp.query.filter_by(order_id=order_id).first()
    # 查询支付信息
    payment = Payment.query.filter_by(order_id=order_id).first()

    # 计算总金额
    total_amount = sum(item.product.base_price * item.quantity for item in order_items)
    if dp:
        total_amount -= dp.amount
    if payment and payment.discount_price:
        total_amount -= payment.discount_price

    return render_template(
        "Starbucks.html",
        store_no=store.store_no,
        store_name=store.store_name,
        order=order,
        order_items=order_items,
        dp=dp,
        payment=payment,
        total_amount=total_amount
    )


# 路由：/user/<user_id> 显示用户所有订单
@app.route('/user/<int:user_id>')
def user_orders(user_id):
    user = User.query.get_or_404(user_id)
    # 获取用户所有订单
    orders = Order.query.filter_by(user_id=user_id).all()

    # 为每个订单计算总金额并关联相关数据
    order_list = []
    for order in orders:
        store = Store.query.get(order.store_id)
        items = OrderItem.query.filter_by(order_id=order.id).all()
        total = sum(item.product.base_price * item.quantity for item in items)
        dp = Dp.query.filter_by(order_id=order.id).first()
        if dp:
            total -= dp.amount
        payment = Payment.query.filter_by(order_id=order.id).first()
        if payment and payment.discount_price:
            total -= payment.discount_price

        order_list.append({
            'order': order,
            'store': store,
            'total': total,
            'item_count': len(items)
        })

    return render_template(
        "user_orders.html",
        user=user,
        order_list=order_list
    )


if __name__ == "__main__":
    app.run()