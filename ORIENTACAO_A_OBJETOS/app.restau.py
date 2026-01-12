from modelos.restaurante import Restaurante
from modelos.cardapio.pratos import Prato
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Caseira')
bebida_suco = Bebida('Suco de laranja', 5.00, '300ml')
bebida_suco.aplicar_desconto()
prato_bife = Prato('Bife acebolado', 25.00, 'Bife com cebolas douradas na manteiga.')
prato_bife.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim de leite', 10.00, 'Pequeno')
restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_bife)
restaurante_praca.adicionar_ao_cardapio(sobremesa_pudim)

restaurante_pizza = Restaurante('pizzaria Bella', 'Pizza')

restaurante_mexico = Restaurante('El Mexicano', 'Comida Mexicana')

restaurante_mexico.alternar_status()

def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()


#Condição usada para que essa função só seja executada quando o arquivo for executado diretamente, e não quando for importado como módulo em outro arquivo.
#Pois quando importamos um módulo, através de outro código, o python exacuta automáticamente todo o código que está no módulo importado, o que pode causar bugs.
#o import é como "ligar um aparelho na tomada" e el já funcionar automaticamente, sem precisar apertar nenhum botão.
#O " if __name__ == '__main__': " funciona como um botão de ligar, só exacutará se você apertar esse botão.   

