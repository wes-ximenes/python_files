nome = input('Seu nome: ')
renda = int(input('Quanto é sua renda: '))
empdisp = renda/100*30
print ('Valor disponível para emprestimo R$ {:.2f}'.format(empdisp))
casa = int(input('Valor da casa: '))
anos = int(input('Em quantos anos pretende pagar: '))
parcela = anos*12
valorp = (casa/parcela)
print ('Ficará em {} vezes de R$ {:.2f}'.format(parcela,valorp))
if valorp <= empdisp:
    print('Emprestimo aprovado {}!'.format(nome))
else:
    print('Emprestimo negado {}! Valor de parcela excedeu o valor compatível a renda de R$ {:.2f}'.format(nome,renda))    
    