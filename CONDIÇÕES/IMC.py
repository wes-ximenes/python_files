peso = float(input('Qual seu peso (kg)? '))
altura = float(input('Qual sua altura (m)? '))
imc = peso/(altura**2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[43mAbaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[30;42mPeso ideal!\033[m')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('\033[43mObesidade\033[m')
else:
    imc >= 40
    print('\033[30;41mObesidade mórbida\033[m')    
              