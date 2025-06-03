sexo = input('Digite o sexo [M/F]: ')
masc = 0
fem = 0

while sexo == 'M' or 'F':
    sexo = input('Digite o sexo [M/F]: ').upper()
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        fem += 1
    elif sexo == '0':
        break      
    else:
        print('Informação incorreta, favor responder com [M/F]')

print(f'Tivemos um total de {masc} homens e {fem} mulheres.')                

