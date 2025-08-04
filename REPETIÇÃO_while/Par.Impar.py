#Jogo de par ou impar, o jogo continua até você perder pro bot
import random

while True:
    lista = [1,2,3,4,5]
    random.shuffle(lista)
    user = input('Escolha, Par ou Impar? ').lower()
    bot = ''

    if user == 'par':
        bot = 'impar'
    elif user == 'impar':
        bot = 'par'

    if user != 'par' and user != 'impar':
        print('Não reconhecido')
        break    


    num = int(input('Escolha um número de 1 a 5: '))
    numbot = random.choice(lista)
    print(f'O bot escolheu: {numbot}')
    soma = num + numbot
    print(f'Soma: {soma}')
    result = ''

    if soma % 2 == 0:
        result = 'par'
    else:
        result = 'impar' 

    if result == user:
        print(f'Você venceu! Deu {result}')
    else:
        print(f'Você perdeu! Deu {result}')   
        break        
