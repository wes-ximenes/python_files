

from fastapi import FastAPI, Query
import requests


app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint acima criado para testar se a aplicação está rodando corretamente.
    Para testar, rode a aplicação localmente com o comando: uvicorn main:app --reload
    '''
    return {'Hello':'World!'}


@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint criado para ver os cardápios dos restaurantes disponíveis na API REST.
    Se nenhum restaurante for especificado, retorna os dados completos da API.
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
            })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else:
        return {"Erro":f'{response.status_code} - {response.text}'}
    
'''
-Para rodar a aplicação localmente, use o comando: uvicorn main:app --reload

-Com o endereço local, voce pode chamar a rota que criamos, por exemplo: http://127.0.0.1:8000/api/restaurantes/

-Para acessar o cardápio de um restaurante específico, adicione o parâmetro de consulta no endpoint ?restaurante=NomeDoRestaurante

-Caso queira ver todas as rotas disponiveis, acesse a documentação automática gerada pelo FastAPI em: http://127.0.0.1:8000/docs (basta colocar o 'docs' no endpoint)

-Para parar a aplicação local, use Ctrl + C no terminal onde o uvicorn está rodando.

-Sempre verificar em qual pasta o terminal está, para rodar o uvicorn na pasta correta.

-Aconselha-se o uso de um ambiente virtual(venv) para instalar as dependências do projeto, evitando conflitos com outras bibliotecas instaladas globalmente.
'''    
