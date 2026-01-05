from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Caseira')
restaurante_praca.adicionar_avaliacao('Wesley', 6.5, 'Excelente comida!')
restaurante_praca.adicionar_avaliacao('Ana', 5.5, 'Ótimo atendimento.')
restaurante_praca.adicionar_avaliacao('Carlos', 9.2, 'Comida boa, mas o ambiente poderia ser melhor.')

restaurante_pizza = Restaurante('pizzaria Bella', 'Pizza')
restaurante_pizza.adicionar_avaliacao('Mariana', 4.8, 'Deliciosas pizzas!')
restaurante_pizza.adicionar_avaliacao('João', 7, 'Demorou muito para entregar.')
restaurante_pizza.adicionar_avaliacao('Lucas', 7.5, 'Melhor pizza da cidade!')

restaurante_mexico = Restaurante('El Mexicano', 'Comida Mexicana')

restaurante_mexico.alternar_status()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()


#Condição usada para que essa função só seja executada quando o arquivo for executado diretamente, e não quando for importado como módulo em outro arquivo.
#Pois quando importamos um módulo, através de outro código, o python exacuta automáticamente todo o código que está no módulo importado, o que pode causar bugs.
#o import é como "ligar um aparelho na tomada" e el já funcionar automaticamente, sem precisar apertar nenhum botão.
#O " if __name__ == '__main__': " funciona como um botão de ligar, só exacutará se você apertar esse botão.   

