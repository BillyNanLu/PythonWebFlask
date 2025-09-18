from flask import Flask, jsonify
app = Flask(__name__)

# 1. 创建路由 /add/<int:a>/<int:b>，计算并返回 a + b 的结果（例如访问 /add/3/5 返回 "8"）。
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"<p>sum = {a + b}</p>"



#  2. 根据字典books实现一组简单的Restful图书管理路由：
'''
GET /books 返回所有图书列表
GET /books/<int:id> 返回指定 ID 的图书详情
POST /books/<book_name> 模拟添加图书（返回 "Book added"）
'''
# 经典小说字典，键为ID，值为书名
books = {
    1: "《战争与和平》",
    2: "《红楼梦》",
    3: "《三国演义》",
    4: "《水浒传》",
    5: "《西游记》",
    6: "《哈姆雷特》",
    7: "《悲惨世界》",
    8: "《百年孤独》",
    9: "《巴黎圣母院》",
    10: "《红与黑》",
    11: "《安娜·卡列尼娜》",
    12: "《复活》",
    13: "《飘》",
    14: "《老人与海》",
    15: "《傲慢与偏见》"
}

@app.get('/books')
def get_all_books():
    return jsonify([{"id": id, "name": name} for id, name in books.items()])

@app.get("/books/<int:book_id>")
def get_book(book_id):
    if book_id in books:
        return jsonify({book_id: books[book_id]})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.post("/books/<book_name>")
def add_book(book_name):
    new_id = max(books.keys()) + 1
    books[new_id] = book_name
    return jsonify({"message": "Book added", "id": new_id, "name": book_name})



if __name__ == "__main__":
    app.run(debug=True, port=5000)
