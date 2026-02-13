'''
Conceito de herança: A herança é um dos pilares da programação orientada a objetos, 
que permite criar novas classes (chamadas de classes filhas ou subclasses) a partir de classes existentes (chamadas de classes mães ou superclasses).

Exemplificamos abaixo de maneira abstrata, uma classe mãe chamada 'Jogador',
que representa um jogador genérico com atributos como altura, velocidade, passe, chute, drible e precisão, e métodos como passar() e chutar().

Em seguida criamos duas classes filhas: JogadorGoleiro e JogadorLinha.
A classe JogadorGoleiro herda as características da classe Jogador e tem um método específico chamado agarrar(), que é exclusivo para goleiros.
Já a classe JogadorLinha herda apenas as características da classe Jogador, não tem nenhum método específico, então usamos o comando pass para indicar que a classe é vazia.
'''


class Jogador:  #Classse mãe ou superclasse | Todo jogador independente da posição tem as mesmas características, então a classe mãe é uma classe genérica para representar um jogador qualquer.
    def __init__(self, altura, velocidade, passe, chute, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.chute = chute
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print("Mirar")
        print("O jogador passou a bola")
        
    def chutar(self):
        print("Mirar")
        print("O jogador chutou a bola")  

class JogadorGoleiro(Jogador):  #Classe filha ou subclasse | O goleiro tem as mesmas características de um jogador comum, mas tem uma função diferente,
    # então ele herda as características da classe mãe nos parenteses e pode usar as funções dela, e tem uma função específica para ele.
    def agarrar(self):
        print("Pular")
        print("O goleiro agarrou a bola") 

class JogadorLinha(Jogador):
    pass  #A classe JogadorLinha é uma classe filha que herda as características da classe mãe, mas não tem nenhuma função específica para ela,
# então usamos o comando pass para indicar que a classe está vazia, ela apenas terá disponível as funções contidas na classe mãe que ela herdou.



jogador1 = JogadorGoleiro(1.90, 80, 50, 30, 40, 60) #Criando um objeto da classe JogadorGoleiro, passando os atributos necessários para o construtor da classe mãe.
jogador2 = JogadorLinha(1.80, 90, 70, 80, 90, 85)

jogador1.passar() #O jogador1 é um goleiro, mas ele pode usar a função passar() da classe mãe, porque ele herda as características da classe mãe.
jogador2.chutar() #O jogador2 é um jogador de linha, mas ele pode usar a função chutar() da classe mãe, porque ele herda as características da classe mãe.

jogador1.agarrar() #Apenas o jogador1, que é um goleiro, pode usar a função agarrar(), porque ela é específica para goleiros e não está presente na classe mãe.
#O jogador2, que é um jogador de linha, não pode usar essa função.