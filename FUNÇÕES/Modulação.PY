#Modulação é o processo de dividir o código em partes menores e reutilizáveis, chamadas módulos. Para poder chamar apenas pelo nome do módulo, sem precisar copiar todo o código.

def soma (*n):
    total = 0
    for valor in n:
        total += valor
    return total


def multiplicacao (*n):
    total = 1
    for valor in n:
        total *= valor
    return total


def fatorial (num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
    
print(soma(5,10,15,20))
print(multiplicacao(5,10,2))
print(fatorial(7))
