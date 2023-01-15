'''Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.'''


def print_name(name):
    print(f"Hello, {name}")

my_names = ["Alex","Olga","Max","Denis","Nick"]

for name in my_names:


    print_name(name)

