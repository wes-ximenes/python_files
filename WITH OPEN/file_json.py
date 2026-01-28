#Manipulando arquivos JSON com o módulo 'json'.

import json

dicionario = { #criando um dicionário para converter em JSON.
    'Nome': 'Wesley',
    'Idade': 27,
    'Cidade': 'Recife-PE'
}

with open ('dados.json', 'w') as arquivo:
    json.dump(dicionario, arquivo) #json.dump() escreve o 'dicionario' no 'arquivo' em formato JSON.

with open ('dados.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo) #json.load() lê o conteúdo do 'arquivo' e o converte de JSON para um dicionário Python, para que possa ser impresso.
    print(dados_lidos)