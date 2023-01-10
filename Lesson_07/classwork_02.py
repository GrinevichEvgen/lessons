'''Написать функцию, которая будет вызывать задержку выполнения программы случайным образом
от 1-й до 5-ти секунд. Написать декоратор, который будет выводить на печать
время выполнения этой функции (end_time - start_time).'''



import random
from  time import sleep
from datetime import datetime
def my_decorator(func):
    def silencer():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(end_time - start_time)
    return silencer

@my_decorator
def my_gun():
    delay = random.randint(1, 5)
    sleep(delay)

if __name__ == "__main__":
    my_gun()