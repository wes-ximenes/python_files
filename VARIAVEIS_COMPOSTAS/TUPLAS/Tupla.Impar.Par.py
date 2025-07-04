tupla = ()
for c in range(4):
    num = int(input('Digite um número: '))
    tupla += (num,) #A forma correta de guardar números em uma tupla
print(tupla)  

tuplaPar = ()
tuplaImpar = ()

for n in tupla:
    if n % 2 == 0:
        tuplaPar += (n,)
        
    else:
        tuplaImpar += (n,)
        
print(f' Pares: {tuplaPar}')
print(f' Impares: {tuplaImpar}')