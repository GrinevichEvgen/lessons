import requests

url = 'https://raw.githubusercontent.com/GrinevichEvgen/lessons/master/LICENSE'

response = requests.get(url)
with open('license.txt', 'wb') as file:
    file.write(response.content)

print(response.content)
