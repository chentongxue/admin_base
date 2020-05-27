# 一个最基础的管理后台
集成了 `Flask-Login`  `Flask-SQLAlchemy`，并且带HTML界面的管理后台。
HTML模板来源： `https://coderthemes.com/greeva/layouts/vertical/index.html`

## 运行过程  
### 创建配置文件
复制 `config.ini` 为 `config.cfg`  
配置数据库连接，格式如下
```
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@host/database_name'
```
例：
```
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/test'
```

### 安装依赖
```
pip install -r requirements.txt
```

### 创建数据库
```
python manager.py create_database
```

### 创建管理员
```
python manager.py create_admin admin 123456
```

### 运行
```
python manager.py runserver
```
