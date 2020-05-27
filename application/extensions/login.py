# coding=utf-8
from flask_login import LoginManager
from application.models.admin import Admin


login_manager = LoginManager()


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.filter_by(admin_id=admin_id).first()


login_manager.login_view = "login.index"
