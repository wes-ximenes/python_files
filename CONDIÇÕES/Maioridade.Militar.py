nome = input('Digite seu nome: ')
nasc = int(input('Ano de nascimento: '))
ano_atual = 2025
idade = ano_atual - nasc
dif = 18-idade
if ano_atual - nasc < 18:
    print('{} anos, faltam {} anos para se alistar'.format(idade,dif))
elif idade == 18:
    print('{} anos, é tempo de se alistar'.format(idade)) 
else:
    ano_atual - nasc > 18
    print('{} anos, já devia ter se alistado, está {} anos atrasado'.format(idade, abs(dif)))    
