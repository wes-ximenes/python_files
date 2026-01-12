from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preço, tamanho):
        super().__init__(nome, preço) #A classe Bebida herda os atributos item e preço da classe ItemCardapio, e adiciona o atributo tamanho, exclusivo da classe bebidas.
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.item} - R$ {self.preço:.2f}\nTamanho: {self.tamanho}'
    
    def aplicar_desconto(self): #implementação do método abstrato da classe pai ItemCardapio.
        self._preço -= self._preço * 0.05