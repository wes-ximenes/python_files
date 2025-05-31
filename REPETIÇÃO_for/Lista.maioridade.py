s = 0
for c in range(0,7):
    idade = int(input('Digite o ano que você nasceu: '))
    if 2025-idade<18:
        print('{} - De menor'.format(idade))
    else:
        print('{} - De maior'.format(idade)) 
        s = s + 1 
print('Número de maiores: {}'.format(s))               
print('FIM')         
  