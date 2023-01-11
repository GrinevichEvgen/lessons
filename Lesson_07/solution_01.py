'''Используя условие первой задачи из урока, проверить то же самое только для коней.'''

first = [3,6]
last = [4,5]

def chess(first, last):
    return 'YES' if abs(first[0] - last[0]) == 1 and abs(first[1] - last[1]) == 2 \
        else 'NO'

print(chess(first , last))


