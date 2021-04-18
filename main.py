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
    code = PasswordField('Код подтверждения', validators=[DataRequired()])
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
    student = [['-', 'Фёдор', 'Соколов', '03.04.2004', 'м', 'example@example.com', '2(2294)749-81-06', 'Соколов Олег'],
               ['-', 'Дарья', 'Иванова', '15.12.2004', 'ж', 'vaherrygi@yopmail.com', '07(421)267-29-65', 'Иванов Андрей'],
               ['-', 'Максим', 'Ковалёв', '01.05.2004', 'м', 'alvis.hahn@gmail.com', '48(245)268-13-67', 'Ковалёв Олег'],
               ['-', 'Кирилл', 'Новиков', '02.11.2004', 'м', 'williamson.fern@jast.com', '18(836)996-61-63', 'Новиков Владимир'],
               ['-', 'Мария', 'Нечаева', '15.07.2004', 'ж', 'schimmel.zaria@terry.net', '275(091)289-31-61', 'Нечаев Сергей']]
    length = len(student)
    return render_template('mainmenu.html', title='Помощник учителя', classes=c, students=student, a=length)


@app.route('/classes')
def classes():
    c = [['-', '10Б'], ['-', '10Г'], ['-', '10Д'],
         ['-', '9Б'], ['-', '9Г'], ['-', '9Д'],
         ['-', '8Б'], ['-', '8Г'], ['-', '8Д'],
         ['-', '7Б'], ['-', '7Г'], ['-', '7Д'],
         ['-', '6Б'], ['-', '6Г'], ['-', '6Д'],
         ['-', '5Б'], ['-', '5Г'], ['-', '5Д']]
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


@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title='Обратная связь')


@app.route('/remind')
def remind():
    reminds = [['-', '10.12.2020', '19:32', 'ДЗ'], ['-', '09.11.2021', '7:34', 'Школа']]
    length = len(reminds)
    return render_template('remind.html', title='Напоминания', rem=reminds, a=length)


@app.route('/links')
def links():
    link = [['-', 'ДЗ', '19:32', 'http://127.0.0.1:8080/program'], ['-', 'Школа', '7:34', 'http://127.0.0.1:8080/program']]
    length = len(link)
    return render_template('links.html', title='Ссылки', rem=link, a=length)


@app.route('/notes')
def notes():
    note = [['-', 'ДЗ', '19:32'], ['-', 'Школа', '7:34']]
    length = len(note)
    return render_template('notes.html', title='Заметки', rem=note, a=length)


if __name__ == '__main__':
    #db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')