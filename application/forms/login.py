# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import fields, validators
from application.models.admin import Admin


class LoginForm(FlaskForm):
    username = fields.StringField(u'用户名', [validators.DataRequired(u'用户名不能为空')])
    password = fields.PasswordField(u'密码', [validators.DataRequired(u'密码不能为空')])

    @property
    def admin(self):
        return Admin.query.filter_by(username=self.username.data).first()

    def validate_username(self, field):
        if not self.admin:
            raise validators.ValidationError(u'用户不存在')

    def validate_password(self, field):
        if self.admin and not self.admin.check_password(field.data):
            raise validators.ValidationError(u'密码错误')
