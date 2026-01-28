# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = [x for x in lista if x % 2 == 0] #o x antes do for é o valor que será adicionado na nova lista e o x depois do for é o valor que está sendo iterado na lista original
# print(numeros_pares)

# with open ('dados.json', 'w') as arquivo:
#     arquivo.write('{"nome": "Wesley", "idade": 27, "cidade": "Recife"}')


with open ('dados.json', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
