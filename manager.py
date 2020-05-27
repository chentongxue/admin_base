# coding=utf-8
import sqlalchemy
from flask_script import Manager

from application import create_app
from application.extensions.database import db
from application.models.admin import Admin


app = create_app('../config.cfg')
manager = Manager(app)


@manager.command
def create_admin(username, password):
    """
    创建管理员账号
    :param username:
    :param password:
    :return:
    """
    Admin.create(username, password)


@manager.command
def create_database():
    """
    创建数据库
    :return:
    """
    tmp = app.config['SQLALCHEMY_DATABASE_URI'].split('/')
    db_name = tmp.pop()
    engine_config = '/'.join(tmp)
    engine = sqlalchemy.create_engine(engine_config)
    engine.execute('CREATE DATABASE `%s` CHARACTER SET utf8 COLLATE utf8_general_ci;' % db_name)
    db.create_all()


if __name__ == '__main__':
    manager.run()
