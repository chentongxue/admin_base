# coding=utf-8
from flask import Blueprint, render_template
from flask_login import login_required
from application.forms.login import LoginForm
from application.models.admin import Admin


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('frontend/index.html')


@frontend_blueprint.route('/test_form', methods=['GET', 'POST'])
@login_required
def test_form():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('frontend/test_form.html', form=form)


@frontend_blueprint.route('/test_table', methods=['GET', 'POST'])
@login_required
def test_table():
    data = Admin.query.paginate()
    return render_template('frontend/test_table.html', data=data)
