import requests

def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:
        dados = requests.get(url)
        resposta = dados.json()
        real = resposta['rates']['BRL']
        euro = resposta['rates']['EUR']
        libra = resposta['rates']['GBP']
        peso = resposta['rates']['ARS']
        return f"1 USD = {real:.2f} BRL | {euro:.2f} EUR | {libra:.2f} GBP | {peso:.2f} ARS"

    except:
        return "Não foi possível realizar a conversão de valores."

print(get_moedas())