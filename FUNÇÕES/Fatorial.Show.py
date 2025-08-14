#FUNÇÃO QUE DA O FATORIAL DE UM NÚMERO, SE SHOW FOR TRUE, ELE MOSTRA TODA OPERAÇÃO, SENÃO ELE DARÁ APENAS O RESULTADO.
def fatorial (n, show=False):
        f = 1
        for c in range(n, 0, -1):
            if show: #Se show for true:
                if c > 1: #Se o contador for menor que 1, ele mantem o print do multiplicador "x"
                    print(f'{c} x ', end='')
                else: #Senão ele retorna o "=" para dar o resultado
                    print(f'{c} = ', end='')      
            f *= c
        return f

#programa principal

print(fatorial(6, show=True))