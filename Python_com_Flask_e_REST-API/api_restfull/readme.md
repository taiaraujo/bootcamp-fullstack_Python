# API RESTFULL

##### API desenvolvida com o método flask_restful. 

Nela é possivel gerenciar dois registros.

[1] resgistro de desenvovedores com id, nome e habilidades. 

[2] uma lista de habilidades.

## Funções

  1. Por meio do pacote api_restfull.app.Developer:
    
    a. exibe dados de um determinado desenvolvedor(a) de acordo com o id inserido utilizando o método 'GET'
    
    b. altera dados de um determinado desenvolvedor(a) de acordo com o id inserido utilizando o método 'PUT'
    
    c. deleta dados de um desenvolvedor(a) de acordo com o id inserido utilizando o método 'DELETE'

  2. Por meio do pacote api_restfull.app.DeveloperLists:
    
    a. insere dados de um novo desenvolvedor(a) no registro utilizando o método 'POST'
    
    b. exibe o registro completos de desenvolvedores 

  3. Por meio do pacote api_restfull.skills.Skills:

    a. retorna a lista completa de habilidades registradas utilizando o método 'GET'
    
    b. inseri uma nova hibilidade na lista utilizando o método 'POST'

  4. Por meio do pacote api_restfull.skills.ModifySkills:
    
    a. altera uma habilidade de acordo com o id inserido utilizando o método 'PUT'
    
    b. deleta uma habilidade de acordo com o id inserido utilizando o método 'DELETE'
