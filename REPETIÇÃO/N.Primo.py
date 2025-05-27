n1 = int(input('Digite um número: '))
primo = True #Assume que é primo, só é dividido por 1 e por ele mesmo. Teremos que provar o contrário no 'for'.
for c in range(2,n1): #Vai testar todas as divisões de 2 até o n1, pois 1 já não é primo.
    if n1 % c == 0:
        primo = False #Se ele encontrar alguma divisão no intervalo do contador, ele vai transofrmar primo em 'false' e vai parar o programa.
        break
if primo: #Se chegar até aqui e não dar break, é porque ele não achou divisão e primo permanece 'true'.
    print('É primo!')
else:
    print('Não é primo')
