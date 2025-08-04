somaidade = 0
mediaidade = 0
#-------------------#
maioridadehomem = 0
nomevelho = None
#-------------------#
totmulher20 = 0
#-------------------#
for c in range(0,4):
    nome = input(f'Nome da {c+1}º pessoa: ')
    idade = int(input(f'Idade da {c+1}º pessoa: '))
    sexo = input(f'Sexo da {c+1}º pessoa [M/F]: ').upper()
    print('--------------------------------')

    somaidade += idade # '+=' serve para resumir que a variavel em questão receberá a soma dela mesma, com a outra, para não precisar repetir o mesmo nome após o '='.

    if c == 1 and sexo in 'Mm': #Se estamos na primeira pessoa, e ela for do sexo masculino ('M' ou 'm'), ele receberá a 'maioridadehomem' e 'nomevelho'. E dará sequencia ao elif.
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem: #Se a pessoa é homem ('M' ou 'm') e a idade for maior que a idade atual registrada, então ela receberá o 'maioridadehomem'.
        maioridadehomem = idade
        nomevelho = nome   

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1  # '+=' serve para resumir que a variavel em questão receberá a soma dela mesma, com a outra, para não precisar repetir o mesmo nome após o '='.

mediaidade = somaidade / 4
print(f'A media das idades foi de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo, são {totmulher20} mulheres abaixo de 20 anos')