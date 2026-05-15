import sqlite3

estoque = sqlite3.connect('estoque.db')
cursor = estoque.cursor()

# cursor.execute(
#     '''
# CREATE TABLE IF NOT EXISTS carros (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     marca TEXT NOT NULL,
#     ano INTEGER NOT NULL,
#     preco REAL NOT NULL
#     )
# '''
# )

# cursor.execute(
#     '''
# INSERT INTO carros (nome, marca, ano, preco) VALUES
#     ('Civic', 'Honda', 2020, 90000),
#     ('Corolla', 'Toyota', 2019, 85000),
#     ('Model 3', 'Tesla', 2021, 190000),
#     ('Celta', 'Chevrolet', 2012, 28000),
#     ('Gol', 'Volkswagen', 2015, 35000),
#     ('Clio', 'Renault', 2014, 30000),
#     ('Pajero', 'Mitsubishi', 2016, 100000)
# '''
# )

# cursor.execute(
#     '''
# CREATE TABLE IF NOT EXISTS vendas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     carro_id INTEGER NOT NULL,
#     data_venda TEXT NOT NULL,
#     valor_venda REAL NOT NULL,
#     FOREIGN KEY (carro_id) REFERENCES carros(id)
#     )
# '''
#) #FOREIGN KEY é declarada para estabelecer um relacionamento entre a tabela vendas e a tabela carros, ela garante que o id do carro vendido exista na tabela carros, mantendo a integridade referencial do banco de dados.

# cursor.execute('''
# INSERT INTO vendas (carro_id, data_venda, valor_venda) VALUES
#     (1, '2024-01-15', 88000),
#     (2, '2025-02-20', 83000),
#     (3, '2026-02-10', 185000),
#     (4, '2025-04-05', 27000),
#     (5, '2023-05-12', 34000)
# '''
# )

# estoque.commit()  #commit é o comando usado para salvar as alterações feitas no banco de dados.

# cursor.execute('SELECT * FROM carros')  #Comando SQL para selecionar todos os registros da tabela carros.
# carros = cursor.fetchall()

# for carro in carros: #fetchall() é o comando que recupera todos os registros retornados pela consulta SQL executada.
#     print(f'ID: {carro[0]}, Nome: {carro[1]}, Marca: {carro[2]}, Ano: {carro[3]}, Preço: R${carro[4]:.2f}')

# cursor.execute('SELECT * FROM vendas')
# vendas = cursor.fetchall()
# for venda in vendas:
#     print(f'ID: {venda[0]}, Carro ID: {venda[1]}, Data da Venda: {venda[2]}, Valor da Venda: R${venda[3]:.2f}')

# estoque.close()  #close é o comando para fechar a conexão com o banco de dados, liberando os recursos utilizados.