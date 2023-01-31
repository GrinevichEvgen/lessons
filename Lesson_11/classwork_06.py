'''Создать функцию для поиска всех пользователей в возрасте от X до Y лет.'''

import sqlite3
def select_user(age1: str, age2: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE age BETWEEN ? AND ?;
           """,
           (age1, age2)
       )
       session.commit()

   selection = cursor.fetchall()
   print(selection)