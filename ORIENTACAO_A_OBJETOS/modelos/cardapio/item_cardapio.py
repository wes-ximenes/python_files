from abc import ABC, abstractmethod #importa ABC (Abstract Base Class) e abstractmethod do módulo abc para criar uma classe abstrata.
#classe abstrata é uma classe que não pode ser instanciada diretamente, servindo como um molde para outras classes.

class ItemCardapio(ABC):
    def __init__(self, nome, preço):
        self._nome = nome.title()
        self._preço = preço

    @abstractmethod
    def aplicar_desconto(self): #método abstrato, depois de criado deve ser implementado por todas as subclasses, se não, o código não funcionará.
        pass

    #Criar um método e fazer com que ele funcione de forma diferente em cada subclasse, é o conceito de ´POLIMORFISMO´.