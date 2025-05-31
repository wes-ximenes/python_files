# Entrada do usuário
a1 = int(input("Digite o primeiro termo da PA: ")) #primeiro termo
r = int(input("Digite a razão da PA: ")) #de quanto em quanto ele vai contar

# Exibe os 10 primeiros termos da PA
print("\nOs 10 primeiros termos da PA são:")
for c in range(10):
    termo = a1 + c * r
    print(termo)

#Ele irá contar de 'r' em 'r' 10 vezes