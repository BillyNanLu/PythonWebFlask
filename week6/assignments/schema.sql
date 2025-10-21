-- 创建用户表
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建商店表
CREATE TABLE stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_no TEXT NOT NULL,
    store_name TEXT NOT NULL,
    address TEXT
);

-- 创建产品表
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    base_price REAL NOT NULL,
    description TEXT
);

-- 创建订单表
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_number TEXT NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    order_time TIMESTAMP NOT NULL,
    invoice_code TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (store_id) REFERENCES stores (id)
);

-- 创建订单项表
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    details TEXT,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

-- DP
CREATE TABLE dp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    method TEXT NOT NULL,
    code TEXT,
    amount REAL,
    details TEXT,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);

-- 创建支付表
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    method TEXT NOT NULL,
    code TEXT,
    amount REAL DEFAULT 0.00,
    discount_price REAL,
    discount_details TEXT,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);



-- 插入示例数据
INSERT INTO users (name) VALUES ('BillyLu');
INSERT INTO users (name) VALUES ('GenieJT');

INSERT INTO stores (store_no, store_name, address)
VALUES ('55523', '临港港城新天地店', '上海市浦东新区茉莉路港城新天地225弄67号');
INSERT INTO stores (store_no, store_name, address)
VALUES ('54574', '星巴克臻选咖啡酒坊', '上海市黄浦区北京东路99号地上1楼L101A室');
INSERT INTO stores (store_no, store_name, address)
VALUES ('545XX', '上海烘焙工坊', '上海市静安区南京西路789号N110至N201单元');

INSERT INTO products (name, base_price, description) VALUES
('星巴克经典咖啡混选中杯单杯MTDP', 24.90, ''),
('星巴克星冰乐混选大杯单杯MTDP', 27.90, ''),
('焦糖玛奇朵中杯', 34.00, '经典咖啡'),
('焦糖玛奇朵大杯', 37.00, '经典咖啡'),
('馥芮白中杯', 35.00, '经典咖啡'),
('馥芮白大杯', 38.00, '经典咖啡'),
('摩卡大杯', 36.00, '经典咖啡'),
('摩卡中杯', 33.00, '经典咖啡'),
('美式咖啡中杯', 27.00, '经典咖啡'),
('美式咖啡大杯', 30.00, '经典咖啡'),
('椰子丝绒燕麦拿铁中杯', 36.00, '经典咖啡'),
('椰子丝绒燕麦拿铁大杯', 39.00, '经典咖啡'),
('海盐焦糖风味冰镇浓缩中杯', 36.00, '经典咖啡'),
('海盐焦糖风味冰镇浓缩大杯', 39.00, '经典咖啡'),
('抹茶星冰乐中杯', 29.00, '星冰乐'),
('抹茶星冰乐大杯', 32.00, '星冰乐'),
('摩卡可可碎片星冰乐中杯', 33.00, '星冰乐'),
('摩卡可可碎片星冰乐大杯', 36.00, '星冰乐'),
('巧克力风味星冰乐中杯', 29.00, '星冰乐'),
('巧克力风味星冰乐大杯', 32.00, '星冰乐'),
('冰摇红莓黑加仑茶中杯', 23.00, '冰摇茶'),
('冰摇红莓黑加仑茶大杯', 26.00, '冰摇茶'),
('冰摇桃桃乌龙茶中杯', 29.00, '冰摇茶'),
('冰摇桃桃乌龙茶大杯', 32.00, '冰摇茶'),
('焙茶拿铁中杯', 26.00, '茶拿铁'),
('焙茶拿铁大杯', 29.00, '茶拿铁'),
('抹茶拿铁中杯', 26.00, '茶拿铁'),
('抹茶拿铁大杯', 29.00, '茶拿铁'),
('红茶拿铁中杯', 26.00, '茶拿铁'),
('红茶拿铁大杯', 29.00, '茶拿铁'),
('香烤白汁大虾芝士薄饼', 32.00, '烘培&三明治'),
('滇香菌菇牛肉法棍三明治', 29.00, '烘培&三明治'),
('烤法式火腿鸡蛋三明治', 23.00, '烘培&三明治'),
('培根芝士蛋堡', 25.00, '烘培&三明治'),
('火腿芝士可颂', 23.00, '烘培&三明治'),
('经典菠萝包', 16.00, '烘培&三明治'),
('千粹抹茶生巧蛋糕', 36.00, '蛋糕'),
('经典提拉米苏蛋糕', 35.00, '蛋糕'),
('经典瑞士卷', 29.00, '蛋糕');


-- billy 1
INSERT INTO orders (order_number, user_id, store_id, order_time, invoice_code)
VALUES ('7111', 1, 1, '2025-05-29 11:26:23', '212841aa2204eb39b6d20');
INSERT INTO order_items (order_id, product_id, quantity, details)
VALUES (1, 1, 1, '中/冰/焦糖玛奇朵'),
       (1, 33, 1, '');
INSERT INTO dp (order_id, method, code, amount, details)
VALUES (1, 'Meituan', '770******927', 1.00, 'DCT_1o1_MT activation');
INSERT INTO payments (order_id, method, code, amount, discount_price, discount_details)
VALUES (1, 'Alipay', '015******035', 3.00, 0.03,'支付宝优惠:¥0.03');


-- billy 2
INSERT INTO orders (order_number, user_id, store_id, order_time, invoice_code)
VALUES ('7198', 1, 2, '2025-07-19 13:53:59', '215782aw2876cp43c6c99');
INSERT INTO order_items (order_id, product_id, quantity, details)
VALUES (2, 18, 1, ''),
       (2, 6, 1, '');
INSERT INTO payments (order_id, method, code, amount, discount_price, discount_details)
VALUES (2, 'WeChat', '015******955', 0.00, 0.00, '微信优惠:¥0.00');


-- GenieJT的订单1
INSERT INTO orders (order_number, user_id, store_id, order_time, invoice_code)
VALUES ('8234', 2, 3, '2025-06-15 09:45:12', '216395bc3789df56e7a12');
INSERT INTO order_items (order_id, product_id, quantity, details)
VALUES (3, 5, 1, '中/热/标准糖'),
       (3, 31, 1, '加热');
INSERT INTO dp (order_id, method, code, amount, details)
VALUES (3, 'Eleme', '881******345', 2.50, '新用户首单立减');
INSERT INTO payments (order_id, method, code, amount, discount_price, discount_details)
VALUES (3, 'WeChat', '026******789', 57.50, 2.50, '微信支付优惠:¥2.50');


-- GenieJT的订单2
INSERT INTO orders (order_number, user_id, store_id, order_time, invoice_code)
VALUES ('8567', 2, 1, '2025-08-03 15:30:45', '217842de4567fg89h0i1');
INSERT INTO order_items (order_id, product_id, quantity, details)
VALUES (4, 16, 1, '大/少冰/少糖'),
       (4, 38, 1, ''),
       (4, 36, 1, '');
INSERT INTO payments (order_id, method, code, amount, discount_price, discount_details)
VALUES (4, 'Alipay', '037******123', 97.00, 5.00, '支付宝会员折扣:¥5.00');

