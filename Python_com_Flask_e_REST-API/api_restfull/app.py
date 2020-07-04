import json

from flask import Flask, request
from flask_restful import Resource, Api
from api_restfull.skills import Skills, ModifySkills

app = Flask(__name__)
api = Api(app=app)

# lista de desenvolvedores :: com id, nome e habilidades
developers = [
    {'id': 0, 'name': 'Natalia', 'skills': ['Python', 'Numpy', 'Flask']},
    {'id': 1, 'name': 'Floribela', 'skills': ['Python', 'Numpy', 'Flask']},
    {'id': 2, 'name': 'Astrogilda', 'skills': ['Java', '.NET', 'nodeJS']},
]


# tratamento individual de acordo com o id
class Developer(Resource):
    # recebe o id pela URN e exibe os dados do desenvolvedor solictado
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = f'Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return response

    # substitui o valor já existente no dicionário 'developers' pelo inserido pelo usuário
    def put(self, id):
        try:
            response = json.loads(request.data)
            developers[id] = response
        except IndexError:
            message = f'Não foi possui modificar registro, Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return response

    # deleta o dicionário da lista de 'developers' de acordo com o id inserido na URN
    def delete(self, id):
        try:
            developers.pop(id)
            response = {'status': 'sucesso', 'message': 'Registro Excluido'}
        except IndexError:
            message = f'Não foi possui excluir registro, Desenvolvedor de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return response

    def post(self):
        return {'status': 'sucesso'}


# tratamento geral da lista de developers
class DevelopersLits(Resource):
    # inseri um novo desenvolvedor na lista 'developers'
    def post(self):
        response = json.loads(request.data)
        index = len(developers)
        response['id'] = index
        developers.append(response)
        return developers[index]

    # exibe os dados de todos os desenvolvedores presentes na lista 'developers'
    def get(self):
        return developers


# adicionando parametros de rota
api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(DevelopersLits, '/dev/')
api.add_resource(Skills, '/skills/')
api.add_resource(ModifySkills, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
