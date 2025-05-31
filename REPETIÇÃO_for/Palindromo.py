#Palíndromo é uma frase ou palavra que quando escrita de trás pra frente, não tem alterações na leitura.
frase = input('Digite uma frase: ').strip().upper() #strip para retirar qualquer espaço no começo e no fim da string.
palavras = frase.split() #split para separar a string por palavras.
junto = ''.join(palavras) #join para juntar as palavras separadas, nesse caso juntou sem nada '', para ficar tudo uma palavra só.
inverso = '' #variavel em branco, irá receber valor no 'for'.

for letra in range(len(junto)-1,-1,-1): #o range será no comprimento(len) da string, ele irá de -1(para começar antes da primeira letra), -1 (até onde vai contar), -1 (para contar regredindo).
    inverso += junto[letra] #Inverso, que era uma variavel em branco, irá receber e somar com o junto.

if junto == inverso:
    print('É um palíndromo') 

print(junto, '|',inverso)
