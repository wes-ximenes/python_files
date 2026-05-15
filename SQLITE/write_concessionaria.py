import sqlite3

estoque = sqlite3.connect('estoque.db')
cursor = estoque.cursor()

# cursor.execute("UPDATE vendas SET carro_id = 85 WHERE id = 36;")
# cursor.execute("UPDATE vendas SET carro_id = 86 WHERE id = 37;")
# cursor.execute("UPDATE vendas SET carro_id = 87 WHERE id = 38;")
# cursor.execute("UPDATE vendas SET carro_id = 88 WHERE id = 39;")
# cursor.execute("UPDATE vendas SET carro_id = 89 WHERE id = 40;")

# estoque.commit()


# cursor.execute('''
# SELECT * FROM vendas'''
# )
# vendas = cursor.fetchall()
# for venda in vendas:
#     print(venda)

cursor.execute('SELECT carros.preco, vendas.valor_venda FROM carros JOIN vendas ON carros.id = vendas.carro_id')
 #JOIN é usado para combinar registros de duas ou mais tabelas com base em uma condição relacionada entre elas, nesse caso,
 # a condição é carros.id = vendas.carro_id, que relaciona o id do carro na tabela carros com o carro_id na tabela vendas.

resultados = cursor.fetchall()
for preco, valor_venda in resultados:
    print(f'Preço do carro: R${preco:.2f}, Valor da venda: R${valor_venda:.2f}')


# estoque.commit()