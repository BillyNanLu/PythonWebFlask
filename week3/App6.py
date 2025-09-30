import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

# 创建一个表格,users(user_id, username, email) user_id is primary key
with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

# 插入三条数据
cur.execute(
    "INSERT INTO users (username,email) VALUES (?, ?)",
    ("小明", "123@qq.com"),
)

cur.execute(
    "INSERT INTO users (username,email) VALUES (?, ?)",
    ("小张", "456@qq.com"),
)

connection.commit()
connection.close()
