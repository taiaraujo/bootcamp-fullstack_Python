from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# lista de desenvolvedores :: com id, nome e habilidades
developers = [
    {'id': 0, 'name': 'Natalia', 'skills': ['Python', 'Numpy', 'Flask']},
    {'id': 1, 'name': 'Rodrigo', 'skills': ['Python', 'Numpy', 'Flask']}
]

# tratamento individual de acordo com o id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    # recebe o id pela URN e exibe os dados do desenvolvedor solictado
    if request.method == 'GET':
        try:
            response = developers[id]
            return jsonify(response)
        except IndexError:
            message = f'Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)

    # substitui o valor já existente no dicionário 'developers' pelo inserido pelo usuário
    elif request.method == 'PUT':
        try:
            response = json.loads(request.data)
            developers[id] = response
        except IndexError:
            message = f'Não foi possui modificar registro, Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)

    # deleta o dicionário da lista de 'developers' de acordo com o id inserido na URN
    elif request.method == 'DELETE':
        try:
            developers.pop(id)
            response = {'status': 'sucesso', 'message': 'Registro Excluido'}
        except IndexError:
            message = f'Não foi possui excluir registro, Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)


# tratamento geral da lista de developers
@app.route('/dev/', methods=['POST', 'GET'])
def developers_list():
    # inseri um novo desenvolvedor na lista 'developers'
    if request.method == 'POST':
        response = json.loads(request.data)
        index = len(developers)
        response['id'] = index
        developers.append(response)
        return jsonify(developers[index])
    # exibe os dados de todos os desenvolvedores presentes na lista 'developers'
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
