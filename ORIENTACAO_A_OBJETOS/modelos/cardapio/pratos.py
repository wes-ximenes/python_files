#HERANÇA - criando a classe prato, que herda atributos da classe ItemCardapio.

from modelos.cardapio.item_cardapio import ItemCardapio #importando a classe cardapio, para herdar dela, conseguir usar os atributos e metodos dela.

class Prato(ItemCardapio): #com a classe ItemCardapio nos parenteses, vamos usar os atributos e métodos dela dentro da classe Prato, isso é herança.
    def __init__(self, item, preço, descricao):
        super().__init__(item, preço) #super() serve para chamar o método __init__ da classe PAI (ItemCardapio), assim herdando os atributos item e preço.
        self.descricao = descricao #descricao é um atributo específico da clase prato, então não usamos o super() aqui.
#basicamente etamos informando que a clase prato, é dependente da classe ItemCardapio, ou seja, prato é um tipo de item do cardápio.   
# 
    def __str__(self):
        return f'{self.item} - R$ {self.preço:.2f}\nDescrição: {self.descricao}'   

    def aplicar_desconto(self): #implementação do método abstrato da classe pai ItemCardapio.
        self._preço -= self._preço * 0.08  


        