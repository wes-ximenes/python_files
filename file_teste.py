# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = [x for x in lista if x % 2 == 0] #o x antes do for é o valor que será adicionado na nova lista e o x depois do for é o valor que está sendo iterado na lista original
# print(numeros_pares)

#=======================================================================================================
#criando arquivos com with open ('w' = white)
# with open ('dados.json', 'w') as arquivo:
#      arquivo.write('{"nome": "Wesley", "idade": 27, "cidade": "Recife"}')

# #lendo o arquivo criado, com with open ('r' = read)
# with open ('dados.json', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#=======================================================================================================
# target = 33
# small = []
# bigger = []
# list = [1, 5, 10, 15, 20, 25, 30, 35, 40, 51, 59]

# for i in list:
#     if i < target:
#         small.append(i)
#     elif i > target:
#         bigger.append(i)

# print("Small numbers:", small)
# print("Bigger numbers:", bigger)  

#=======================================================================================================
# produtos = None
# total = 0

# while produtos != 0:
#     produtos = float(input("Digite o valor do produto: "))
#     total += produtos
    
# print(f'Total da compra: R$ {total}')

#=======================================================================================================
from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.mainloop()