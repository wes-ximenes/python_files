#Trabalhando com API REST usando a biblioteca requests
#API REST funciona como um serviço web que permite a comunicação entre sistemas através de requisições HTTP.
#A biblioteca requests em Python facilita o envio de requisições HTTP e o tratamento das respostas

import requests #biblioteca requests é usada para fazer requisições HTTP em Python, para buscar dados na web.
import json #biblioteca json é usada para trabalhar com dados em formato JSON (JavaScript Object Notation), que é um dicionário leve e fácil de ler e escrever.

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" #URL da API REST que fornece dados em formato JSON

response = requests.get(url) #O método da requests, o get(), envia uma requisição para a URL especificada, para obter os dados dela.

if response.status_code == 200: #Verifica se a requisição foi bem-sucedida (código de status 200 indica sucesso).
    dados_json = response.json() #O método .json() converte a resposta da API, que está em formato JSON, em um dicionário Python.
    dados_restaurante = {} #Criando um dicionário vazio para armazenar os dados dos restaurantes.
    for item in dados_json:
        nome_restaurante = item["Company"] #Acessa o valor associado à chave "Company" em cada item do JSON.
        if nome_restaurante not in dados_restaurante: #Verifica se o restaurante já está no dicionário que criamos
            dados_restaurante[nome_restaurante] = [] #Se não estiver, adiciona o nome do restaurante como chave no dicionário, com um valor inicial de lista vazia.

        dados_restaurante[nome_restaurante].append({  #Adiciona um novo dicionário à lista do restaurante correspondente, contendo os detalhes de cada item.
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f"Erro ao acessar a API. Código de status: {response.status_code}")

# print(dados_restaurante['McDonald’s']) #imprime os dados do restaurante McDonald's

for nome_restaurante, dados in dados_restaurante.items(): #esse for vai percorrer o dicionário dados_restaurante, onde nome_restaurante é a chave (nome do restaurante) e dados é o valor (lista de itens do restaurante).
    nome_do_arquivo = f'{nome_restaurante}.json' #Cria o nome do arquivo JSON com base no nome do restaurante.
    with open(nome_do_arquivo, 'w') as arquivo: #Cria e abre um arquivo com o nome especificado, o 'w' indica que o arquivo será aberto para escrita (white), os arquivos criados ficarão disponíveis na pasta do projeto.
        json.dump(dados, arquivo, indent=4) #Usa a função json.dump() para escrever os dados do restaurante no arquivo JSON, com uma indentação de 4 espaços para melhor legibilidade.

    #esse 'for', num geral, cria um arquivo JSON separado para cada restaurante, contendo os itens do menu e seus detalhes, ele separa os dados por restaurante e salva cada conjunto de dados em um arquivo distinto.

    print(f'Arquivo {nome_do_arquivo} criado com sucesso.') #Informa que o arquivo foi criado com sucesso.            