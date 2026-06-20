import requests 

url = "https://api.exchangerate-api.com/v4/latest/EUR"

dados = requests.get (url)

resposta = dados.json()

moeda_estrangeira = resposta['rates']['EUR']
valor_moeda_base = 1 / resposta['rates']['BRL']

print(f" {valor_moeda_base:.2f} EUR = 1 BRL")