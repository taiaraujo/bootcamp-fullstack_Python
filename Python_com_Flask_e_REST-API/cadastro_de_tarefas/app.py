"""  ------------> MISSÕES A SEREM CUMPRIDAS NESSE CÓDIGO <------------ #
# [OK] gerenciar um cadastro de tarefas
# [OK] listar todas as tarefas
# [OK] incluir novas tarefas
# [ok] consultar um tarefa atraves de um id
# [ok] alterar um status atevés de um id
# [ok] excluir uma tarefa
# [OK] nenhuma outra alteração deverá ser permitida além da mudança de status """


from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# lista de tarefas
tasks = [
    {'id': 0, 'responsible': 'Natália', 'task': 'tratamento de dados', 'status': 'iniciado'},
    {'id': 1, 'responsible': 'Marcelo', 'task': 'analise de requisitos', 'status': 'concluido'},
    {'id': 2, 'responsible': 'Monalisa', 'task': 'front-end', 'status': 'espera'},
    {'id': 4, 'responsible': 'Joana Darque', 'task': 'back-end', 'status': 'iniciado'}
]

# tratamento individual de acordo com o id
@app.route('/tasks/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def modify_by_id(id):
    # recebe o id pela URN e exibe os dados da tarefa correspondente
    if request.method == 'GET':
        try:
            response = tasks[id]
        except IndexError:
            message = f'Tarefa de ID-{id} não encontrada'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Entre em contato com o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)

    # modifica status da tarefa requisitada através do id
    elif request.method == 'PUT':
        try:
            response = json.loads(request.data)
            tasks[id]['status'] = response['status']
            response = tasks[id]
        except IndexError:
            message = f'Tarefa de ID-{id} não encontrada'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Entre em contato com o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)
    # exclui a tarefa com o id repassado pela URN
    elif request.method == 'DELETE':
        try:
            tasks.pop(id)
            response = {'status': 'sucesso', 'message': 'tarefa excluída com sucesso'}
        except IndexError:
            message = f'Erro na exclusão, tarefa de ID-{id} não encontrada'
            response = {'status': 'error_0', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Entre em contato com o administrador da API'
            response = {'status': 'error_1', 'message': message}
        return jsonify(response)


# tratamento geral da lista de 'tasks'
@app.route('/tasks/', methods=['GET', 'POST'])
def modify_list():
    # inserir uma nova tarefa a lista
    if request.method == 'POST':
        response = json.loads(request.data)
        index = len(tasks)
        response['id'] = index
        tasks.append(response)
        return jsonify(tasks[index])
    # retorna todos os itens da lista de tarefas
    elif request.method == 'GET':
        return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
