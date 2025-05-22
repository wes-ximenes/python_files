nome = input('Qual o seu nome? ')
nome = nome.lower()
if nome == 'wesley':
    print('Que nome bonito!')
elif nome == 'igor' or nome == 'duda':
    print('Nome bastante popular!')    
else:
    print('Que nome normal')
print('Tenha um bom dia {}!'.format(nome))    
