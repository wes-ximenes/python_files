num = 0
soma = num
quant = 0
while num != 999:
    num = int(input('Digite um número: '))
    
    if num == 999:
        break
    else:
        soma += num
        quant += 1

print(f'{quant} números solicitados, e a soma deles foi: {soma}')    
