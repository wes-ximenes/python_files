i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p): #f+1, pois ele sempre irá parar de contar um numero antes do final.
    print(c)
print('FIM')    


#for c in range(0,10): #'c' Seria a variável de contagem.

#(0,10) - É de quanto ele começa a contar e onde ele terminará.
#(0,10,2) - O terceiro número indica o ritmo, ele irá contar de 2 em 2.
#(10,0,-1) - Ele irá contar subtraindo 1, fazendo uma contagem regressiva.