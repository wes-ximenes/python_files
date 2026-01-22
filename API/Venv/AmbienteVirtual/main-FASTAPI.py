#Criando um endpoint simples usando FastAPI, mas ele apenas funciona localmente.
#Para subir a rota pra nuvem, é preciso de um hosting, para hospedar a aplicação.

from fastapi import FastAPI, Query #importando as classes FastAPI e Query da biblioteca fastapi
import requests


app = FastAPI() #Alocando a classe FastAPI na variavel app

@app.get('/api/hello') #definindo uma rota GET na URL /api/hello    #o @.get cria uma rota.
def hello_world():
    '''
    Endpoint acima criado para testar se a aplicação está rodando corretamente.
    Para testar, rode a aplicação localmente com o comando: uvicorn main:app --reload
    '''
    return {'Hello':'World!'} #Quando a rota for acessada, retorna um dicionario com a mensagem "Hello: World!"


@app.get('/api/restaurantes/') #rota
def get_restaurantes(restaurante: str = Query(None)): #definindo uma função que recebe um parâmetro de consulta opcional 'restaurante' (pode ser None)
    '''
    Endpoint criado para ver os cardápios dos restaurantes disponíveis na API REST.
    Se nenhum restaurante for especificado, retorna os dados completos da API.
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" #URL da API REST que fornece dados em formato JSON

    response = requests.get(url) #O método da requests, o get(), envia uma requisição para a URL especificada, para obter os dados dela e aloca na variavel response.

    if response.status_code == 200: #Verifica se a requisição foi bem-sucedida (código de status 200 indica sucesso).
        dados_json = response.json() #O método .json() converte a resposta da API, que está em formato JSON, em um dicionário Python.
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json: #percorrendo cada item do JSON
            if item['Company'] == restaurante: #verifica se o nome do restaurante no item atual é igual ao nome do restaurante fornecido como parâmetro no endpoint
                dados_restaurante.append({ #Adiciona um novo dicionário à lista do restaurante correspondente, contendo os detalhes de cada item.
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
            })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante} #Retorna um dicionário com o nome do restaurante e o cardápio correspondente. 
    else:
        return {"Erro":f'{response.status_code} - {response.text}'}
    
'''
-Para rodar a aplicação localmente, use o comando: uvicorn main:app --reload

-Com o endereço local, voce pode chamar a rota que criamos, por exemplo: http://127.0.0.1:8000/api/restaurantes/

-Para acessar o cardápio de um restaurante específico, adicione o parâmetro de consulta no endpoint ?restaurante=NomeDoRestaurante

-Caso queira ver todas as rotas disponiveis, acesse a documentação automática gerada pelo FastAPI em: http://127.0.0.1:8000/docs (basta colocar o 'docs' no endpoint)

-Para parar a aplicação local, use Ctrl + C no terminal onde o uvicorn está rodando.
'''    
