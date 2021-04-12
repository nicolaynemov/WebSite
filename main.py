import datetime

import sqlalchemy
from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from data import db_session
from data.db_session import SqlAlchemyBase
#from data.users import User


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def ma():
    return 'Миссия Колонизация Марса'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', title='Авторизация', form=form)


@app.route('/registration')
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/program')
def prog():
    return render_template('mainmenu.html', title='Помощник учителя')


if __name__ == '__main__':
    #db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')