#programa irá pedir 5 números aleatórios, jogar numa lista e informar: Maior e o menor; posições dele no indice da lista utilizando enumerate.
lista = []
maior = None
menor = None

for n in range (0, 5):

    num = int(input(f'Digite um valor para posição {n}: '))
    lista.append(num)

    if maior is None or num > maior: #Se a variável 'maior' ainda for 'none', ou o 'num' do imput for maior que ela, 'maior' receberá o 'num' do input.
        maior = num
        
    if menor is None or num < menor:
        menor = num

print(f'Lista: {lista}')         
print(f'Maior elemento: {maior}, na posição ',end='') 
for indice, valor in enumerate(lista): #Vai jogar cada indice e seu valor, do enoumerate na lista, pro if abaixo.
    if valor == maior:
        print(f'{indice}... ', end='')
print()        
print(f'Menor elemento: {menor}, na posição ',end='') 
for indice, valor in enumerate(lista):
    if valor == menor:
       print(f'{indice}... ', end='') 
print()       
