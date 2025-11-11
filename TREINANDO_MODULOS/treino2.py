#Para utilizar uma função que está em outro arquivo, usamos o comando import + nome do arquivo (sem o .py), eles precisam estar na mesma pasta.
#Isso ajuda a diminuir o tamanho do código principal, deixando ele mais organizado e fácil de entender.

from uteis import fat 
from uteis import dobro
from uteis import formatString as fs


escolha = int(input("Escolha uma opção:\n1 - Fatorial\n2 - Dobro\n3 - Formatação de Texto\n"))
if escolha == 1:

    n = int(input("Digite um número: "))
    print('-'*30)
    resultado = fat.fatorial(n)

    print(f'O fatorial de {n} é {resultado}')

elif escolha == 2:

    v = int(input("Digite um número para dobrar: "))
    print('-'*30)
    d = dobro.dobrar(v)
    print(f'O dobro de {v} é {d}')


elif escolha == 3:
    texto = input('\nDigite o texto: ')
    print('-'*30)
    minusculo, maiusculo, capitalized = fs.format(texto)
    print('\nMinusculo: ', minusculo)
    print('\nMaiusculo: ', maiusculo)
    print('\nCapitalized: ', capitalized)


