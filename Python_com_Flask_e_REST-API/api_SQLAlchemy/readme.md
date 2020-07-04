# API SQLAchemy

##### API com construção, gerenciamento de banco de Dados e requisição de autenticação para acesso, utilizando SQLAlchemy.

## Funções

1. api_SQLalchemy.models:

    a. cria as regras e as tabelas para a base de dados

2. api_SQLalchemy.utils (arquivo para testes no terminal): 

    a. manipula a tabela pessoas
    
        i. inseri novos registros
        
        ii. consulta registros na base de dados
        
        iii. altera registros
        
        iv. deleta registros
        
    b. mostra exemplo de criação de usuários para liberação de acesso
        
 3. api_SQLAlchemy.app >> manipulação do banco de dados 'Atividades'
 
    a. api_SQLAlchemy.app.Pessoa
    
        i. consulta dos dados de uma pessoa específica por meio de seu 'nome' utilizando o método 'GET'
    
        ii. modifica dados de uma determinada pessoa utilizando o método 'PUT'
    
        iii. deleta o registro de uma pessoa pelo sei 'nome' através do método 'DELETE'

    b. api_SQLAlchemy.app.ListaPessoas
    
        i. exibi toda a lista de 'pessoas' (método 'GET')
        
        ii. inseri um novo registro na tabela 'pessoa' (método 'POST')

    c. api_SQLAlchemy.app.Atividades
    
        i. consulta dos dados de uma pessoa específica por meio de seu 'nome' utilizando o método 'GET'
    
        ii. modifica dados de uma determinada atividades utilizando o método 'PUT'
    
        iii. deleta o registro de uma pessoa pelo sei 'nome' através do método 'DELETE'

    
    d. api_SQLAlchemy.app.ListasAtividades
    
        i. exibi toda a lista de 'atividades' (método 'GET')
        
        ii. inseri um novo registro na tabela 'atividades' (método 'POST')
