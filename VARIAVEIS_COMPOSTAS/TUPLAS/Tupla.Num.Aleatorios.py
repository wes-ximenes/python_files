import random

num = [49,11,9,17,60,33,23,51,3,5,8,20]
random.shuffle(num)

escolhidos = random.sample(num, k=5) #o K é um elemento de estatistica obrigatorio para definir a quantidade de escolhas que o choices irá pegar
#também pode ser substituito pelo random.sample(), a diferença é que o choices pode repetir elementos e o sample não repete.
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Tupla aleatória: {escolhidos}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

maior = None
for c in escolhidos:
    if maior is None or c > maior: #Se o 'maior' ainda for none ou o contador for maior que 'maior', 'maior' vai armazenar o C, até achar outro número maior que ele.
        maior = c
print(f'O maior número da tupla: {maior}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

menor = None
for c in escolhidos:
    if menor is None or c < menor:
        menor = c
print(f'O menor número da tupla: {menor}')        
