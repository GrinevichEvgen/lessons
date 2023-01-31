'''Создать программу позволяющую осуществлять поиск по имени или возрасту,
оба параметра вводятся с клавиатуры.'''


import sqlite3


def select_user():
    name = input('Type a name: ')
    age = int(input('Type an age: '))
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE firstname = ? OR age = ?;
        """, (name, age)
                       )
        session.commit()
        selection = cursor.fetchall()
        print(selection)


select_user()