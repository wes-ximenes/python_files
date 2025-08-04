cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze'  #tupla, uma variável com mais de um valor ou string

while True:
    num = int(input('Digite um número entre 0 e 15: '))
    if 0 <= num <= 15: #verifica se o número está dentro do intervalo entre 0 e 15
        print('Número válido! ', end='')
        break
    else:
        print('Número inválido, tente novamente. ', end='')

print(f'Você digitou o número {cont[num]}') #A tupla funciona como um índice [0, 1, 2, 3, ...], a que criamos possui um indice de 0 a 15 elementos
                                            #Que são os números que permitimos que sejam digitados, o 'num' irá buscar o elemento que está no indice da tupla.     
        
    