'''Создать python функцию, которая создает таблицу user, для примера использовать слайд №12.
Запустить функцию и проверить, что создался файл базы данных.'''

import sqlite3


def create_user():
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           CREATE TABLE user (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   firstname VARCHAR,
   lastname VARCHAR,
   email VARCHAR,
   password VARCHAR,
   age INTEGER,
   datetime DATETIME
);

""")
       session.commit()

create_user()