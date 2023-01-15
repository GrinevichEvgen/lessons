'''Создать список состоящий из отдельных единичных символов, преобразовать список в строку,
 инвертировать строку и вывести на печать.'''




arr = ['a', 'b', 'c', 'd']
str = ''
for i in range(len(arr)):
    str += arr[i]
reserved = ''.join(reversed(str))
print(reserved)