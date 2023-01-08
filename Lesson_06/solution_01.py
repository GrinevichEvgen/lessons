text =  input ("Введите текст : ")
my_spis = (text.split())

print(max(my_spis, key=len))

a = {x for x in my_spis if my_spis.count(x)>1}
print(*a)