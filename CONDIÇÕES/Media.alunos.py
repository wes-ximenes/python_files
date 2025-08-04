nome = input('Nome do aluno: ')
nome = nome.capitalize()
av1 = float(input('Nota av1: '))
av2 = float(input('Nota av2: '))
media = (av1+av2)/2
if media >= 7:
    print('{} Está aprovado, parabéns!'.format(nome))
elif media >= 5 and media <= 6.9:
    print('{} ficou em recuperação'.format(nome))
else:
    media < 5
    print('{} está reprovado'.format(nome))  
