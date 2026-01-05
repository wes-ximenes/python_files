import time

class Computer:
    #propriedades/ atributos do objeto computador
    def __init__(self, marca, memoriaRam, processador, armazenamento, sistemaOperacional):
        self.marca = marca #o self serve para referenciar o próprio objeto, permitindo chamar os atributos e métodos dentro da classe.
        self.memoriaRam = memoriaRam
        self.processador = processador
        self.armazenamento = armazenamento
        self.sistemaOperacional = sistemaOperacional

    #Métodos são as ações/comportamentos que o objeto pode executar. São funções definidas dentro da classe e que usam self.
    def ligar(self):
        return f'O computador {self.marca} está ligado.'
    
    def desligar(self):
        return f'O computador {self.marca} está desligado.'
    
    def exibir_detalhes(self):
        return (f'Marca: {self.marca}\n'
                f'Memória RAM: {self.memoriaRam}\n'
                f'Processador: {self.processador}\n'
                f'Armazenamento: {self.armazenamento}\n'
                f'Sistema Operacional: {self.sistemaOperacional}')

#instancias da classe Computer, objetos específicos que ocupam espaço na memória.
computador1 = Computer('Dell', '16GB', 'Intel i7', '512GB SSD', 'Windows 10')
computador2 = Computer('Apple', '8GB', 'M1', '256GB SSD', 'macOS Big Sur')
computador3 = Computer('HP', '32GB', 'AMD Ryzen 9', '1TB SSD', 'Windows 11')

print(computador1.ligar())
time.sleep(1.5)
print(computador1.exibir_detalhes())
time.sleep(1.5)
print(computador1.desligar())