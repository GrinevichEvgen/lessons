'''В школе решили набрать три новых класса по программированию.
Так как занятия у них проходят в одно и то же время, было решено выделить кабинет для каждого класса
и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.'''

def count_desk(arr):

    if sum(arr)%2==0:
        return int(sum(arr)/2)
    return int((sum(arr)+1)/2)
arr = list(map(int,input().split()))
print(count_desk(arr))