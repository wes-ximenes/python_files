#guardar vários números numa lista, sem repeti-los e ordenar eles.

lista = []

while True:
    num = int(input('Guarde um valor: '))
    if num == 999:
        break
    if num not in lista:
        lista.append(num)
    else:
        print('Número já adicionado.')

lista.sort()
print(lista)
    