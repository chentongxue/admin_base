# coding=utf-8
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application.forms.login import LoginForm


login_blueprint = Blueprint('login', __name__, url_prefix='/login')


@login_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('frontend.index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.admin)
        return redirect(url_for('frontend.index'))
    return render_template('login/index.html', form=form)


@login_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login.index'))
