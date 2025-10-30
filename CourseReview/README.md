# 🎓 Flask 课程评价系统（Course Review System）

一个基于 **Flask + Tailwind CSS + ECharts** 开发的简易课程评价系统。  

支持用户注册登录、课程评价、评论管理、管理员后台统计等功能。  

GitHub仓库地址：https://github.com/BillyNanLu/PythonWebFlask/tree/main/CourseReview

---

## 🌟 功能概览

### 👨‍🎓 前台（用户端）

- 用户注册 / 登录 / 退出登录

- 查看课程列表与详情

- 对课程进行评分与评论（支持半星显示）

- 修改密码

- 查看与删除自己的评论记录

### 🧑‍💼 后台（管理员端）

- 查看系统总体数据统计（用户数 / 课程数 / 评论数）

- 使用 **ECharts** 展示：
  - 各课程评论数量柱状图
  - 评分分布饼图

- 查看最新评论列表

- 管理课程信息（添加、编辑、删除课程）

- 管理用户与评论（可扩展）



---

## 🏗️ 技术栈

| 技术                 | 说明                         |
| -------------------- | ---------------------------- |
| **Flask**            | Python 轻量级 Web 框架       |
| **Flask SQLAlchemy** | ORM 数据操作层               |
| **MySQL**            | 数据库存储                   |
| **Tailwind CSS**     | 现代响应式前端框架           |
| **Jinja2**           | 模板引擎（用于前后端渲染）   |
| **ECharts**          | 数据可视化（管理员统计图表） |
| **Flash 消息系统**   | 交互提示反馈                 |



---

## 🗂️ 数据库设计

### 1️⃣ 用户表 `user`
| 字段        | 类型        | 说明                   |
| ----------- | ----------- | ---------------------- |
| id          | INT         | 主键                   |
| username    | VARCHAR(50) | 用户名（唯一）         |
| password    | VARCHAR(64) | MD5 加密密码           |
| role        | TINYINT     | 0：普通用户，1：管理员 |
| create_time | DATETIME    | 注册时间               |

### 2️⃣ 课程表 `course`
| 字段        | 类型         | 说明     |
| ----------- | ------------ | -------- |
| id          | INT          | 主键     |
| name        | VARCHAR(100) | 课程名称 |
| teacher     | VARCHAR(50)  | 授课教师 |
| description | TEXT         | 课程简介 |
| create_time | DATETIME     | 创建时间 |

### 3️⃣ 评价表 `review`
| 字段        | 类型     | 说明        |
| ----------- | -------- | ----------- |
| id          | INT      | 主键        |
| user_id     | INT      | 用户ID      |
| course_id   | INT      | 课程ID      |
| rating      | INT      | 评分（1–5） |
| comment     | TEXT     | 评论内容    |
| create_time | DATETIME | 评论时间    |



---

## ⚙️ 项目运行步骤

### 🧩 1. 克隆项目

```bash
git clone https://github.com/yourname/flask-course-review.git
cd flask-course-review
```

### 🐍 2. 创建虚拟环境并安装依赖

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 🧱 3. 初始化数据库

修改 `config.py` 中的数据库连接信息：

```python
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1:3306/course_review
```

创建表结构：

```bash
flask shell
>>> from models import db
>>> db.create_all()
```

### 🚀 4. 启动项目

```bash
flask run
```

访问：

- 前台用户端 👉 http://127.0.0.1:5000
- 管理员端 👉 http://127.0.0.1:5000/admin/dashboard



---

## 📊 管理员 Dashboard

包含三部分信息面板：

1. **系统统计卡片**

   - 用户总数、课程总数、评论总数

2. **ECharts 图表**

   - 📈 各课程评论数量柱状图
   - 🥧 评论评分分布饼图

3. **最新评论列表**

   - 显示最近 5 条评论的课程、用户、内容与评分

   

---

## 💡 项目结构

```bash
CourseReview /
├── app.py                 # 主入口
├── init.sql			   # 数据库文件
├── models.py              # 数据模型定义
├── README.md			   # 项目说明
├── settings.py			   # 配置文件
├── requirements.txt       # 所需依赖包
├── routes/
│   ├── user_routes.py     # 用户相关路由
│   ├── course_routes.py   # 课程与评论功能
│   └── admin_routes.py    # 管理员端功能
├── templates/
    ├── login.html		   # 登录页
    ├── register.html	   # 注册页
│   ├── layout.html        # 用户端主布局
│   ├── home.html          # 用户端主页
│   ├── courses.html       # 课程浏览页
    ├── courses_detail.html# 课程详情与评论页
    ├── profile.html	   # 用户个人中心页
    ├── admin/             # 管理员端页面（含 dashboard）
│   └── components/        # 课程评论星星🌟样式
└── static/
    ├── css/
    ├── images/
    └── js/
```



---

## 🧑‍💻 作者

**Your Name（陆楠 / Nan Lu / Billy）**
 📫 Email: lunan96789@gmail.com
 🌐 GitHub: https://github.com/BillyNanLu