import random
lista = []
nomes = ''
num = 0
while nomes != 'fim':
    nomes = input('Nome:').lower()
    num += 1
    print(f'{num} jogadores(as)')
    if nomes == 'fim':
        break
    lista.append(nomes)
random.shuffle(lista)
equipe1 = lista[0::3]
equipe2 = lista[1::3]
equipe3 = lista[2::3]
print ('Time 1:\033[4;32m {}\033[m'.format(equipe1)) #\033[m colocado no final é para o que vir em sequencia ficar padrão (preto).
print ('Time 2:\033[4;34m {}\033[m'.format(equipe2))
print ('Time 3:\033[4;30m {}\033[m'.format(equipe3))

#CODIGO PARA 3 EQUIPES APENAS

#trabalhando cores:
#Coloca-se o código dentro do print logo após a primeira aspa
#\033[(0;33;44)m (sempre separados por ;)

#Primeiro cod pós colchete: Será o estilo, se ta normal, sublinhada, negrito.
#0 = normal, sem estilo(none)
#1 = negrito (bold) 
#4 = sublinhada (underline)
#7 = negative (inverte as cores, a cor do fundo vem pro texto e vice versa)

#Segundo cod: será qual a cor do texto.
#30 = branco
#31 = vermelho
#32 = verde
#33 = amarelo
#34 = azul
#35 = roxo
#36 = ciano
#37 = cinza

#Terceiro cod: qual será o background(fundo).
#40 = branco
#41 = vermelho
#42 = verde
#43 = amarelo
#44 = azul
#45 = roxo
#46 = ciano
#47 = cinza
#preto = padrão, só não colocar código (\033[m)
#letra preta e fundo braço = \033[7:30m
