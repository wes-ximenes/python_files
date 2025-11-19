import random

print('Bem vindo ao jogo de Adivinhação!')
numero_secreto = random.randint(1, 5)
palpite = 0

while palpite != numero_secreto:
    
    try:
        palpite = int(input('Digite seu palpite (entre 1 e 5): '))
        
        if palpite < 1 or palpite > 5:
            print('Por favor, insira um número entre 1 e 5.')
        elif palpite != numero_secreto:
            print('Errado! Tente novamente.')
        else:
            print('Parabéns! Você adivinhou o número secreto.')    

    except Exception as erro:
        print('Por favor, insira um número válido de 1 a 5.')

            