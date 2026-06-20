from flask import Flask, jsonify, request
from  flask_cors import CORS

app = Flask(__name__)

CORS(app)


produtos = [
    {"id":1,
     "nome":"Notebook Gamer",
     "preco": 4000
     },
    {"id":2,
     "nome":"Cadeira Gamer",
    "preco": 300
    },
    {"id":3,
     "nome":"Monitor",
    "preco": 500
    }
]

@app.route("/listar", methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)

#Criar uma rota e o método POST
@app.route("/criar", methods=['POST'])
def criarProdutos():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    return (produtoNovo),201

@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProdutos(id):
    dados = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto['preco'] = dados['preco']
            return jsonify(dados)
        return jsonify({"mensagem":"ID não encontrado"}),404

@app.route("/apagar/<int:id>", methods=['DELETE'])
def apagarProduto(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify({"mensagem":"Produto removido!"})
    return jsonify({"mensagem":"ID não encontrado"}),404

if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")