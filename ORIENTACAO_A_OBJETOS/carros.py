class Carro: #classe funciona como um molde para criar objetos

    Carros = []

    def __init__(self, nome, marca, cor, ano, preço, status= 'À venda'): # iniciando o objeto com seus atributos, usando o método construtor __init__
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.preço = preço
        self.status = status
        Carro.Carros.append(self)

    def __str__(self): # método especial para representar o objeto como string e não como um endereço de memória
        return f'{self.nome} | {self.marca} | {self.cor} | {self.ano} | R$ {self.preço} | {self.status}'

    def listar_carros(carros): # método criado por mim para listar os carros cadastrados
        for carro in carros:
            print(f'{carro.nome} | {carro.marca} | {carro.cor} | {carro.ano} | R$ {carro.preço} | {carro.status}')
supra = Carro('Supra', 'Toyota', 'Vermelho', 2020, 250000)
camaro = Carro('Camaro', 'Chevrolet', 'Amarelo', 2019, 230000)
lancer = Carro('Lancer', 'Mitsubishi', 'Branco', 2015, 125000) 

Carro.listar_carros(Carro.Carros)

