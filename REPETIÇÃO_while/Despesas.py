despesa = int(input("Digite o valor da despesa (ou 0 para sair): R$ "))
total_despesas = 0

while despesa != 0:
    total_despesas += despesa
    despesa = int(input("Digite o valor da despesa (ou 0 para sair): R$ "))


print(f"O total das despesas é: R$ {total_despesas}")