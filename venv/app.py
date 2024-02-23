import requests

url = 'https://github.com/mbilby/api-restaurante/blob/main/venv/json/restaurante.json'

response = requests.get(url)
if response.status_code == 200:
    json = response.json()
    print(json)
else:
    print(f'Erro de código de status: {response.status_code}')
