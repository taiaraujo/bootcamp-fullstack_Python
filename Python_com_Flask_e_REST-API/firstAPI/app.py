from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# trabalhando com dados json e interação com a URN
@app.route('/<int:id>')
def my_api(id):
    soma = 1 + id
    return jsonify({'id': id, 'name': 'Taia', 'profession': 'Developer'})


# recebendo e trabalhando com valores da URN
@app.route('/soma/<int:n1>/<int:n2>/')
def soma(n1, n2):
    return jsonify({'soma': n1+n2})


# testando a entrada de dados por diferentes métodos
@app.route('/soma2', methods=['POST', 'PUT', 'GET'])
def soma2():
    if request.method == 'POST':
        dados = json.loads(request.data)
        print(dados)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 0
    else:
        total = "nenhum valor informado"

    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
