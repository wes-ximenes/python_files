preço = float(input('Preço do produto R$: '))
pagamento = input('Qual forma de pagamento? ')
if pagamento == '1x':
    preço = preço-(10/100*preço)
    print('O valor ganha 10% de desconto e sairá por R$ {:.2f}'.format(preço))
elif pagamento == '2x':
    print('Valor não ganha desconto, sairá pelo preço real, R$ {:.2f}'.format(preço))  
else:
    pagamento == '3x'
    preço = preço+(20/100*preço) 
    print('Em 3x o valor recebe 20% de juros, sairá por R$ {:.2f}'.format(preço))   
