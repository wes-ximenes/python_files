maior = None #None significa que a variável ainda não tem valor definido, tipo uma casa em branco.
menor = None
for c in range(5):
    peso = int(input(f'Digite o peso da {c+1}ª pessoa: ')) #o 'f' é como se fosse o format, pra ele conseguir chamar a variável dentro do imput.
    
    if maior is None or peso > maior: #Se "maior" ainda não tiver valor OU se o novo "peso" for maior que o atual
        maior = peso #A variavel 'maior' recebe o novo 'peso'.
    if menor is None or peso < menor:
        menor = peso

print(f'O mais pesado foi {maior} kg e o menos pesado foi {menor} kg')
