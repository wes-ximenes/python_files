class Carro:

    Carros = []

    def __init__(self, nome, marca, cor, ano, preço, status= 'À venda'):
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.preço = preço
        self.status = status
        Carro.Carros.append(self)

    def __str__(self):
        return f'{self.nome} | {self.marca} | {self.cor} | {self.ano} | R$ {self.preço} | {self.status}'

    def listar_carros(carros):
        for carro in carros:
            print(f'{carro.nome} | {carro.marca} | {carro.cor} | {carro.ano} | R$ {carro.preço} | {carro.status}')
supra = Carro('Supra', 'Toyota', 'Vermelho', 2020, 250000)
camaro = Carro('Camaro', 'Chevrolet', 'Amarelo', 2019, 230000)
lancer = Carro('Lancer', 'Mitsubishi', 'Branco', 2015, 125000) 

Carro.listar_carros(Carro.Carros)

