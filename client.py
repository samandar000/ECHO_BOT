import requests

BASE_URL = 'https://pardayevsamandar.pythonanywhere.com/api'

data = {'name':'Moto','age':17}

r = requests.post(BASE_URL,json=data)

print(r.json())