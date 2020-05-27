# coding=utf-8
import sqlalchemy as sa

from application.models.base import BaseModelMixin
from application.extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Admin(db.Model, BaseModelMixin, UserMixin):
    admin_id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    username = sa.Column(sa.String(20), nullable=False)
    password_hash = sa.Column(sa.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is read-only')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def create(cls, username, password):
        admin = Admin()
        admin.username = username
        admin.password = password
        db.session.add(admin)
        db.session.commit()
        return admin

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.admin_id
