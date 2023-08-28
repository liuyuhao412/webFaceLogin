from app import create_app
from app import db
from app.models.login import LoginModel

app = create_app('development')
#创建数据库所有表的函数
def create_db(app):
    db.init_app(app),
    with app.app_context():
        db.create_all() 
#删除数据库所有表的函数
def drop_db(app):
    db.init_app(app),
    with app.app_context():
        db.drop_all() 

if __name__ == '__main__':
    # drop_db(app)
    # create_db(app)
    app.run()      #运行代码