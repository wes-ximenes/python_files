#Trabalhando com o banco de dados NoSQL MongoDB usando a biblioteca pymongo em Python.
#MongoDB é um banco de dados orientado a documentos que armazena dados em formato BSON (uma extensão binária do JSON), chave-valor.
#Diferente do banco de dados relacional, o MongoDB não utiliza tabelas e linhas, mas sim coleções e documentos.
#Uma chave pode conter valores simples, arrays ou até documentos aninhados dentro dela.
#Muito usado em apps web e API's por sua flexibilidade e escalabilidade.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") #esse endereço você encontra no site oficial do MongoDB, é o endereço padrão para conectar ao servidor local do MongoDB

db = client["escola"]  # Cria ou conecta ao banco de dados "escola", seria equivalente ao "CREATE DATABASE escola;" em SQL
estudantes = db["estudantes"]  # Cria ou conecta à coleção "estudantes", que seria o mesmo que o comando "CREATE TABLE estudantes (...);" em SQL

estudantes.insert_one({
    "nome": "Igor", "idade": 22, "curso": "Ciencia da Computação"
})  # Insere um documento na coleção "estudantes"

for estudante in estudantes.find():  # Percorre todos os documentos na coleção "estudantes"
    print(estudante)