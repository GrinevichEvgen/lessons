'''Создать функцию, которая позволяет добавлять данные в таблицу user.
 Добавить 5 различных записей.'''


import sqlite3



def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()

create_user("Lena", "Chaika", "Lena.by@gmail.com", "TestPass", 62)
create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
create_user("Roma", "Chaika", "Roma.by@gmail.com", "TestPass", 28)
create_user("Maksim", "Chaika", "Maksim.by@gmail.com", "TestPass", 62)
create_user("Gena", "Chaika", "Gena.by@gmail.com", "TestPass", 35)
create_user("Valera", "Chaika", "Valera.by@gmail.com", "TestPass", 62)