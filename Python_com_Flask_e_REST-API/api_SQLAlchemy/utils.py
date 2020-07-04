from api_SQLAlchemy.models import Pessoas, Usuarios


# insere novos registros na tabela pessoas
def insert(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    print('Cadastro realizado com sucesso')


# consulta a tabela 'pessoas'
def query(nome):
    # retorna todos os registros
    if nome is False:
        pessoa = Pessoas.query.all()
        print(pessoa)
    # retorna um registro específico
    else:
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            print(pessoa.id, pessoa.nome, pessoa.idade)

        except Exception:
            print('Registro não encontrado')


# altera dados já cadastrados
def alter(nome, idade):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.idade = idade
    pessoa.save()


def insere_usuario(login, senha, status):
    usuario = Usuarios(login=login, senha=senha, status=status)
    usuario.save()


def consulta():
    usuario = Usuarios.query.all()
    print(usuario)


# deleta um registro
def delete(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.delete()


if __name__ == '__main__':
    # exemplo de criação de usuários para acesso a API
    insere_usuario(login='admin', senha='admin', status=True)
    insere_usuario(login='root', senha='123', status=False)
    consulta()

    # interação com o usuário >> MENU PRINCIPAL
    '''
    op = int(input('[1] - Consultar\n[2] - Inserir\n[3] - Deletar\n[4] - Alterar \n >> '))

    # ESCOLHA == CONSULTA
    if op == 1:
        op = int(input('[0] - Para registro específico \n[1] - Para todos os registros\n >> '))
        if op == 0:
            name = input('Informe nome: ')
        else:
            name = False
        query(name)
    # ESCOLHA == INSERÇÃO DE DADOS
    elif op == 2:
        try:
            nome = input('Nome >> ')
            idade = int(input('Idade >> '))
            insert(nome=nome, idade=idade)

        except:
            print('Erro na inserção do registro. Verifique seus dados')

    # ESCOLHA == EXCLUSÃO DE DADOS
    elif op == 3:
        nome = input('Nome: ')
        delete(nome=nome)

    # ESCOLHA == ALTERAÇÃO DE DADOS
    elif op == 4:
        try:
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            alter(nome=nome, idade=idade)

        except:
            print('Erro na alteração do registro. Verifique seus dados')

    # ESCOLHA NÃO EXISTENTE NO MENU PRINCIPAL
    else:
        print('Opção inválida')
'''
