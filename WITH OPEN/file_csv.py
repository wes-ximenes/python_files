#Para manipular arquivos CSV (Comma-Separated Values/Valores separados por vírgula) em Python, utilizamos o módulo embutido csv.

import csv

with open ('dados.csv', 'w') as f:
    escritor = csv.writer(f) #diferente do txt, para manipular arquivos csv, precisamos declarar uma variável que utilize o csv.writer() para escrever no arquivo.
    escritor.writerow(['Nome', 'Idade', 'Cidade']) #escrevendo a primeira linha (cabeçalho) do arquivo csv, usando uma lista para representar as colunas.
    escritor.writerow(['Wesley', 27, 'Recife']) #escrevendo a segunda linha do arquivo csv.
    escritor.writerow(['Duda', 24, 'Limoeiro'])

with open ('dados.csv', newline='') as f: #ao abrir arquivos csv para leitura, é recomendado usar o parâmetro newline='' para evitar problemas com quebras de linha.
    #o newline='' instrui o python a não interpretar caracteres de nova linha, o que pode causar linhas em branco extras ao ler o arquivo, tipo um \n a mais.
    leitor = csv.reader(f) #declarando a variável leitor que utiliza o csv.reader() para ler o arquivo csv.
    for linha in leitor: #percorrendo cada linha do arquivo csv.
        print(linha) #imprimindo a linha lida, cada linha é representada como uma lista.    