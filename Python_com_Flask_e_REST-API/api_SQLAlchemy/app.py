from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from api_SQLAlchemy.models import Pessoas, Atividades, Usuarios

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app=app)

"""
# Exemplo de cadastros para acesso em código direto
users = {
    'admin': 'admin',
    'root': '123',
}

# funcao para verificar senha
@auth.verify_password
def verificacao(login, senha):
    print('validando usuario')
    print(users.get(login) == senha)
    if not (login, senha):
        return False
    return users.get(login) == senha
"""


# funcao para verificar senha >> cadastro via banco
# exemplo de cadastro em api_SQLAlchemy.utils
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha, status=True).first()


class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }

        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': 'pessoa não registrada'
            }
        return response

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    def put(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dado = request.json
            if 'nome' in dado:
                pessoa.nome = dado['nome']
            if 'idade' in dado:
                pessoa.idade = dado['idade']
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
            return response

        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Registro não encontrado'}

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    def delete(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            mensagem = f'Registro de {pessoa.nome} excluído com sucesso'
            pessoa.delete()
            return {'status': 'sucesso', 'mensagem': mensagem}

        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Registro não encontrado'}


class ListaPessoas(Resource):
    # para acessar esse metodo é necessario está logado
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    def post(self):
        dado = request.json
        pessoa = Pessoas(nome=dado['nome'], idade=dado['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class Atividade(Resource):
    # retorna uma atividade especifica
    def get(self, nome):
        try:
            atividade = Atividades.query.filter_by(nome=nome).first()
            response = {
                'id_atividade': atividade.id,
                'atividade': atividade.nome,
                'status': atividade.status,
                'pessoa': atividade.pessoa.nome
            }

        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': 'atividade não registrada'
            }
        return response

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    def put(self, nome):
        try:
            atividade = Atividades.query.filter_by(nome=nome).first()
            dado = request.json
            if 'nome' in dado:
                atividade.nome = dado['nome']
            if 'status' in dado:
                atividade.idade = dado['status']
            atividade.save()
            response = {
                'id': atividade.id,
                'atividade': atividade.nome,
                'status': atividade.status,
                'pessoa': atividade.pessoa.nome
            }
            return response

        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Registro não encontrado'}

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    # deleta uma atividade
    def delete(self, nome):
        try:
            atividade = Atividades.query.filter_by(nome=nome).first()
            mensagem = f'Registro de {atividade.nome} excluído com sucesso'
            atividade.delete()
            return {'status': 'sucesso', 'mensagem': mensagem}

        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Registro não encontrado'}


class ListaAtividades(Resource):
    # retorna todas as atividades registradas
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id,
                     'atividade': i.nome,
                     'status': i.status,
                     'pessoa': i.pessoa.nome} for i in atividades]
        return response

    # para acessar esse metodo é necessario está logado
    @auth.login_required
    # adicionando uma nova atividades
    def post(self):
        try:
            dado = request.json
            pessoa = Pessoas.query.filter_by(nome=dado['pessoa']).first()
            atividade = Atividades(nome=dado['nome'], status=dado['status'], pessoa=pessoa)
            response = {
                'ID Pessoa': atividade.pessoa.id,
                'pessoa': atividade.pessoa.nome,
                'atividade': atividade.nome,
                'status': atividade.status
            }
            atividade.save()
            return response

        except:
            return {'status': 'erro', 'mensagem': 'Verifique os dados inseridos.'}


# rotas de acesso
api.add_resource(Pessoa, '/pessoas/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoas/')
api.add_resource(Atividade, '/atividades/<string:nome>/')
api.add_resource(ListaAtividades, '/atividades/')


if __name__ == '__main__':
    app.run(debug=True)
