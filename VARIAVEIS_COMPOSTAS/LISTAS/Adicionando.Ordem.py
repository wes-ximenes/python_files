#PROGRAMA PARA LER 5 NÚMEROS E GUARDA-LOS EM ORDEM, SEM UTILIZAR O 'SORT'. (FORMA ALTERNATIVA)

lista = []

for c in range (0, 5):
    num = int(input('Guarde um valor: '))

    if c == 0 or num > lista[-1]: #Se o contador for igual a 0 ou o 'num' digitado for maior que o ultimo da lista (-1), ele vai adicionar
        lista.append(num)
    else:
        pos = 0 #definindo uma variavel para posição na lista
        while pos < len(lista): #enquanto a posição for menor que o indice(comprimento) da lista:
            if num <= lista[pos]: #Se o número digitado for menor ou igual a posição atual na lista:
                lista.insert(pos, num) #Ele vai inserir o número na posição igual a ele na lista.
                break
            pos += 1 #para ir dando sequencia

print('-=' *30)
print(f'Os valores digitados em ordem foram {lista}')



#Outra maneira:
#for num in range(0, 5):
#    num = int(input('Guarde um valor: ')) 
#    if num not in lista:
#        lista.append(num)
#    else:
#        print('Número já existe')   

#    for indice, num in enumerate(lista):
#        indice = num
#        print(f'{num} adicionado na posição {indice}')

#lista.sort()
#print(f'Sua lista: {lista}')

