#Importações de frameworks
from flask import Flask, jsonify, request 
from flask_cors import CORS

#Criar o nosso app
app = Flask(__name__)
#Habilitar o CORS
CORS(app)

#Criando nosso banco de dados local
produtos = [
    {"id":1,
     "nome":"Notebook Gamer",
     "preco": 4000
     },
     {"id" :2,
      "nome": "Cadeira Gamer",
      "preco": 300
    },
    {"id":3,
     "nome": "monitor Gamter",
     "preco": 500
     }
]

#Criar uma rota
@app.route("/listar", methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)

#Criar uma rota e o método POST
@app.route("/criar", methods=['POST'])
def criarProdutos():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    return (produtoNovo)
    
#Criar uma rota e o método PUT (atualizar)
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProduto(id):
    dados = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto['preco'] = dados ['preco']
            return jsonify(dados)
        

 #criar uma rota e o método DELETE (apagar)
@app.route("/apagar/<int:id>", methods=['DELETE'])
def apagarProduto(id):
    for produto in produtos:
                produtos.remove(produto)
                return jsonify({"mensagem":"Produto removido!"})
    return jsonify({"mensagem": "ID não encontrado"}),404

#Rodar o programa
if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")


