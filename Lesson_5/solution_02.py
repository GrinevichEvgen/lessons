import random as rd

ts = ["Alex","Olga","Max","Denis","Nick"]

rd.shuffle(ts)

for i in range(-1, len(ts)-1):
    print(f'{ts[i]} = {ts[i+1]}')

