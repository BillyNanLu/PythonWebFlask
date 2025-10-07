from settings import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_no = db.Column(db.String(20), nullable=False)
    store_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    base_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_number = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    order_time = db.Column(db.DateTime, nullable=False)
    invoice_code = db.Column(db.String(50))

    # 关系映射
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    store = db.relationship('Store', backref=db.backref('orders', lazy=True))


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    details = db.Column(db.Text)

    # 关系映射
    order = db.relationship('Order', backref=db.backref('items', lazy=True))
    product = db.relationship('Product', backref=db.backref('order_items', lazy=True))


class Dp(db.Model):
    __tablename__ = 'dp'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    method = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50))
    amount = db.Column(db.Float)
    details = db.Column(db.Text)

    order = db.relationship('Order', backref=db.backref('dp_records', lazy=True))


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    method = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50))
    amount = db.Column(db.Float, default=0.00)
    discount_price = db.Column(db.Float)
    discount_details = db.Column(db.Text)

    order = db.relationship('Order', backref=db.backref('payments', lazy=True))