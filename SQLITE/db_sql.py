#sqlite é uma biblioteca nativa do python para trabalhar com bancos de dados relacionais.
#Ela permite criar, conectar e manipular bancos de dados SQLite diretamente a partir do código Python, sem a necessidade de um servidor de banco de dados separado.
#SQLite é leve, fácil de usar e ideal para aplicações pequenas a médias, como aplicativos móveis, protótipos e projetos pessoais.
#Os dados são armazenados em um único arquivo no disco, o que facilita o gerenciamento e a portabilidade do banco de dados.

import sqlite3

connect = sqlite3.connect("escola.db") #.connect é o comando para conectar ou criar o banco de dados, o arquivo escola.db será criado na mesma pasta do script se não existir.
cursor = connect.cursor()#cursor é o objeto que permite executar comandos SQL no banco de dados conectado.

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL DEFAULT 'Desconhecido',
    idade INTEGER)
""")

cursor.execute("""
    INSERT INTO alunos (nome, idade) VALUES
    ('Wesley', 27),
    ('Duda', 24),
    ('Igor', 22)
""")

connect.commit() #commit é o comando usado para salvar as alterações feitas no banco de dados.

cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall()) #fetchall() é o comando que recupera todos os registros retornados pela consulta SQL executada.

connect.close() #close é o comando para fechar a conexão com o banco de dados, liberando os recursos utilizados.