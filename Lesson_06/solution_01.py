'''Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.'''


text =  input ("Введите текст : ")
my_spis = (text.split())

print(max(my_spis, key=len))

a = {x for x in my_spis if my_spis.count(x)>1}
print(*a)