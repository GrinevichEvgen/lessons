'''Создать функцию для поиска всех пользователей с определенным именем.
Запустить функцию и найти хотя бы одного пользователя по имени.'''

import sqlite3


def select_user(firstname: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE firstname = ?;
           """,
           (firstname,)
       )
       session.commit()
       return cursor.fetchone()


print(select_user("Roma"))