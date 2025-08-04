import random

lista = [1,2,3]
bot = random.choice(lista)
escolha = ''
tentativas = 1

while escolha != bot:
    escolha = int(input('Adivinhe o número do bot de 1 a 3: '))
    if escolha != bot:
        tentativas += 1

print(f'Acertou! O bot escolheu {bot}, você usou {tentativas} tentativa(as)!')    