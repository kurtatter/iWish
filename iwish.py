import os
import sqlite3

from flask import Flask
from flask import render_template, flash, redirect, url_for, request, g, session

from models import Wish

app = Flask(__name__)

menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'Добавить мечту', 'url': '/add_wish'}
]

DATABASE = 'wish.db'
SECRET_KEY = 'abraC!ad@da434bra'

app.config.from_object(__name__)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


# Вспомогательная функция для создания таблиц БД
def create_db():
    db = connect_db()
    with app.open_resource('wish.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# Соединение с БД, если оно еще не установлено
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# Закрываем соединение с БД, если оно было установлено
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if not os.path.exists(DATABASE):
    create_db()


@app.route('/')
def index():
    db = get_db()
    dbase = Wish(db)
    wishes = dbase.get_all()
    return render_template('index.html', wishes=wishes, menu=menu)


@app.route("/add_wish", methods=["POST", "GET"])
def add_wish():
    db = get_db()
    dbase = Wish(db)

    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        url = request.form['url']
        description = request.form['description']
        result = dbase.add_wish(title, price, url, description)
        if not result:
            flash('Ошибка добавления мечты', category='error')
        else:
            flash('Мечта добавлена успешно', category='success')
            return redirect(url_for('add_wish'))

    return render_template('add_wish.html', title='Добавить мечту', menu=menu)


@app.route("/edit_wish/<int:id>", methods=['GET', 'POST'])
def edit_wish(id):
    db = get_db()
    dbase = Wish(db)
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        url = request.form['url']
        description = request.form['description']
        result = dbase.edit_wish(id, title, price, url, description)
        if not result:
            flash('Ошибка изменения мечты', category='error')
        else:
            return redirect(url_for('index'))

    return render_template('edit_wish.html', data=dbase.get_wish(id), menu=menu)


@app.route('/delete/<int:id>')
def delete_wish(id):
    db = get_db()
    dbase = Wish(db)
    dbase.delete_wish(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
