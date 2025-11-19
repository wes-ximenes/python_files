n = 0 
lista = []
while n != 999: #Quando impomos um limite no while (999), é chamado de FLAG.
    n = int(input('Digite um número: '))
    if n != 999:
        lista.append(n)

print(f'Você digitou os valores {lista}')