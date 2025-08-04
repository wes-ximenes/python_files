def contador (i, f, p): #inicio / fim / passo
    c = 1
    while c <= f: #enquanto o contador for menor ou igual ao fim, ele continua contando
        print(f'{c+1} ', end='')
        c += p #contador soma com os passos, para percorrer a contagem.


contador(0, 10, 2)        