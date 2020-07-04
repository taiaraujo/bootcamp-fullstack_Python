import json

from flask import request
from flask_restful import Resource


skillsList = ["Python", "Java", "Flask", "PHP"]


# tratamento geral da lista de habilidades
class Skills(Resource):
    # retorna a lista completa de habilidades registradas
    def get(self):
        return skillsList

    # inseri uma nova hibilidade na lista
    def post(self):
        response = json.loads(request.data)
        # verifica se a lista já contém a habilidade inserida, apenas se não conter ela será inserida
        if response not in skillsList:
            skillsList.append(response)
            return skillsList
        else:
            return f"Nossa lista já contém a habilidade: '{response}'"


# tratamento individual de acordo com o id
class ModifySkills(Resource):
    # altera a habilidade passada pelo id
    def put(self, id):
        try:
            response = json.loads(request.data)
            # somente será alterad se a lista não contém nova habilidade
            if response not in skillsList:
                skillsList[id] = response
                return skillsList
            else:
                return f"Nossa lista já contém a habilidade: '{response}'"
        except IndexError:
            return f"Habilidade de ID-{id} não contém na lista"
        except Exception:
            return "Erro desconhecido, falar com o administrador da API"

    # deleta a habilidade requisitada pelo id
    def delete(self):
        try:
            skillsList.pop(id)
            response = {'status': 'sucesso', 'message': 'Registro Excluido'}
        except IndexError:
            message = f'Não foi possui excluir registro, Habilidade de ID{id} não existe'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return response
