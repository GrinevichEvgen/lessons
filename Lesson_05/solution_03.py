'''Написать функцию, которая используя модуль requests скачивает файл
и сохраняет его на файловой системе, функция имеет два параметра:
ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE'''


import requests

url = 'https://raw.githubusercontent.com/GrinevichEvgen/lessons/master/LICENSE'

response = requests.get(url)
with open('license.txt', 'wb') as file:
    file.write(response.content)

print(response.content)
