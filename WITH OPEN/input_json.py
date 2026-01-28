#Criando um programa que coleta informações do usuário e salva em um arquivo JSON

import json

usuarios = [] #para o json funcionar corretamente com os inputs criados, os dicionários precisam ser armazenados numa lista.

while True:
    
    nome = input('Digite seu nome (ou "sair"): ')
    if nome.lower() == 'sair':
        break

    idade = input('Digite sua idade: ')
    if idade.lower() == 'sair':
        break

    curso = input('Digite seu curso: ')
    if curso.lower() == 'sair':
        break



    usuarios.append({ #Criando os dicionários com as informações coletadas e adicionando na lista 'usuarios'. Precisa estar dentro do loop para adicionar múltiplos usuários.
        'nome': nome,
        'idade': idade,
        'curso': curso
    })

# Salvando os dados coletados em um arquivo JSON, e utilizando ferramentas do python como 'encoding' para que o json salve com caracteres especiais corretamente.
with open('usuarios.json', 'w', encoding='utf-8') as arquivo: #encoding='utf-8' para suportar caracteres especiais
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False) #indent=4 para formatar o JSON com indentação de 4 espaços, ensure_ascii=False para permitir caracteres especiais.



