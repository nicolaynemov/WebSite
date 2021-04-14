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
    c = ['10Б', '10Г', '10Д']
    student = [['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Дарья', 'Иванова', '15.12.2004', 'ж', 'example@example.com', '9534837485', 'Иванов Андрей'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],
               ['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '9846734848', 'Соколов Олег'],]
    length = len(student)
    return render_template('mainmenu.html', title='Помощник учителя', classes=c, students=student, a=length)


@app.route('/classes')
def classes():
    c = [['-', '10Б'], ['-', '10Г'], ['-', '10Д']]
    length = len(c)
    return render_template('classes.html', title='Работа с классами', classes=c, a=length)


@app.route('/about')
def about():
    c = [['-', '10Б'], ['-', '10Г'], ['-', '10Д']]
    length = len(c)
    return render_template('about.html', title='Помощь в работе', classes=c, a=length)


@app.route('/account')
def acc():
    return render_template('account.html', title='Аккаунт')


@app.route('/send')
def send():
    a = 'Александ Иванов\nДарья Кузнецова' # передавать получателей как строку с разделителями для отображения
    return render_template('send.html', title='Рассылка', person=a)


if __name__ == '__main__':
    #db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')