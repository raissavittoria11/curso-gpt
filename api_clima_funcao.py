import requests

api_key = "cac3675298344cecca249b7b9fd2febc"

cidade = "Americana"

def get_clima():

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

    try:
        dados = requests.get(url)
        resposta = dados.json()
        temperaturaAtual = resposta['main']['temp']
        descricao = resposta['main'][0]['humidity']
        return f"A temperatura atual é {temperaturaAtual} °C. \nA umidade atual é {umidade} % \nDescrição: {descricao}"
    except:
        

dados = requests.get(url)

resposta = dados.json()

print(resposta)

temperaturaAtual = resposta['main']['temp']
umidade = resposta['main']['humidity']

descricao = resposta['weather'][0]['description']

print(temperaturaAtual)
print(umidade)
print(descricao)
