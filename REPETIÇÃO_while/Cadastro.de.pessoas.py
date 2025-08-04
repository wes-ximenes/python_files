#VAI CONTABILIZAR: DE MAIORES; NUMERO DE HOMENS; MULHERES COM MENOS DE 20 ANOS
#FINALIZA QUANDO VOCÊ DIZ QUE NÃO QUER CONTINUAR

npessoa18 = 0
nhomens = 0
nmulher20 = 0
continuar = ''

while True:
    print('----------------------------------')
    print('CADASTRO DE PESSOAS')
    print('----------------------------------')

    idade = int(input('Idade: '))
    if idade >= 18:
        npessoa18 += 1

    print('----------------------------------')

    sexo = input('Sexo [M/F]: ').lower()
    if sexo == 'm':
        nhomens += 1
    elif sexo == 'f' and idade < 20:
        nmulher20 += 1    

    print('----------------------------------')

    continuar = input('Deseja continuar [S/N]: ').lower()
    if continuar == 'n':
        break

print('----------------------------------')
print(f'Maiores de 18 anos: {npessoa18}')
print(f'Homens: {nhomens}')
print(f'Mulheres com menos de 20 anos: {nmulher20}')
