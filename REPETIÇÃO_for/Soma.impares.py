s = 0
for c in range(0,500+1):
    if c % 2== 1 and c % 3 == 0:
        s = s + c
        print(c)
print('A soma dos números impares multiplos de 3 foi: {}'.format(s))
     