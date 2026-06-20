import requests

import os

api_key = "cac3675298344cecca249b7b9fd2febc"

cidade = "Campinas"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

dados = requests.get(url)

resposta = dados.json()

print(resposta)

temperaturaAtual = resposta['main']['temp']
umidade = resposta['main']['humidity']

descricao = resposta['weather'][0]['description']

print(temperaturaAtual)
print(umidade)
print(descricao)