#Classe abstrata é uma classe que não pode ser instanciada, ou seja, não pode criar objetos diretamente a partir dela. 
#Ela apenas serve como um modelo para outras classes que herdam dela, e geralmente contém métodos abstratos, que são métodos que devem ser implementados pelas classes filhas.
#No exemplo abaixo, temos uma classe abstrata chamada "Animal" com um método abstrato "falar".
#As classes "Cachorro" e "Gato" herdam de "Animal" e implementam o método "falar" de maneira diferente.
#É um exemplo de polimorfismo, onde o mesmo método "falar" tem comportamentos diferentes dependendo da classe que o implementa.

from abc import ABC, abstractmethod #ABC - Abstract Base Class, é uma classe base abstrata que serve como um modelo para outras classes.

class Animal(ABC):

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print("Au au")


class Gato(Animal):

    def falar(self):
        print("Miau")


dog = Cachorro()
dog.falar()