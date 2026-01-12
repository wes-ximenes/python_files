from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preço, tamanho):
        super().__init__(nome, preço)
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.item} | R$ {self.preço:.2f} | Tamanho: {self.tamanho}'
    
    def aplicar_desconto(self): #implementação do método abstrato da classe pai ItemCardapio.
        pass