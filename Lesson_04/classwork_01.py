'''ан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.
'''
from random import randint


my_list = []

x = randint(0, 20)
for i in range(x):
    y = randint(0, 100)
    my_list.append(y)

print(my_list)


result = 0
for element in my_list:
    if element > 10:
        result = result + element

print(result)

