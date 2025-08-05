def Par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um número: '))
if Par(num):
    print('É par!')
else:
    print('É impar!')    
    