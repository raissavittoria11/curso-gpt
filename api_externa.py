import requests as rq

dadosUsuarios = {
    "UsuarioUm": "Murilo"
}

cep = input("Digite o CEP da sua casa: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

resposta = dados.json()

print(f"{dadosUsuarios['UsuarioUm']} mora em {resposta['logradouro']}, bairro {resposta['bairro']}, {resposta['localidade']} - {resposta['uf']}.")