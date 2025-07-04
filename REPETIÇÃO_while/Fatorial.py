num = int(input('Digite um número: '))
grav = num
fat = 1

print(f'{grav}! = ', end='') #Para gravar o número do input antes de começar a contar regressivamente
#end='' -> Serve para que o print sequente siga na mesma linha e não quebre pra linha de baixo.

while num > 0:
    print(num, end='') #Para que ele printe o num antes de partir pra verificação do if, isso impede que ele imprima um 'x' mesmo após o ultimo número
    fat *= num #O fatorial vai receber a multiplicação dele mesmo com o número do input e entrar em loop subtraindo -1 e multiplicando novamente.
    num -= 1

    if num > 0:
        print(f' x ' , end='') #Se o numero ainda for maior que 0, ele irá imprimir o X entre o loop acima.
    else:
        print(f' = {fat}') #Caso chegue no 0, irá imprimir '=' e o resultado final da multiplicação do fat * num .  

