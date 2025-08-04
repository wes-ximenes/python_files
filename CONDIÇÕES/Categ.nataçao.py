nome = input('Nome do atleta: ')
nome = nome.capitalize()
idade = int(input('Idade: '))
if idade <= 9:
    print('{}, Categoria Mirim'.format(nome))
elif idade > 9 and idade <= 14:
    print('{}, Categoria infantil'.format(nome))    
elif idade > 14 and idade <= 19:
    print('{}, Categoria junior'.format(nome))
elif idade > 19 and idade <= 21:
    print('{}, Categoria sênior'.format(nome))
else:
    idade > 21
    print('{} Categoria master'.format(nome))            
