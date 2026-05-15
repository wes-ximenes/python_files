import sqlite3

estoque = sqlite3.connect('estoque.db')
cursor = estoque.cursor()

cursor.execute('DELETE FROM carros')
cursor.execute('DELETE FROM vendas')

estoque.commit()