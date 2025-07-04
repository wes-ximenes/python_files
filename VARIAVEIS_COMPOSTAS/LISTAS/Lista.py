lista = [1,2,3,4]
lista2 = []

#Acrescentando elemento no fim da lista
lista.append(7)
print(f'Append num 7 {lista}')

#Inserindo elementos na lista
lista.insert(0, 9)
print(f'Insert num 9 na posição 0 {lista}')

#Deletando elementos por índice:
#Também pode utilizar o lista.pop(), irá remover o ultimo item se deixar os parenteses em branco.
del lista[2]
print(f'Del index 2 {lista}')

#Deletando elementos pelo nome:
lista.remove(4)
print(f'Remove num 4 {lista}')

#Trocando elementos:
lista[1] = 6
print(f'Trocando 1 pelo 6 {lista}')

for c in range(0, 5):
    lista2.append(int(input('Digite um valor para adicionar a lista2: ')))
print(lista2)    

