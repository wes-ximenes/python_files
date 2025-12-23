class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria): # init serve para inicializar os atributos do objeto, muito usado em classes/ self representa o objeto que está sendo criado, pode ser substituído por qualquer outro nome, como "this", usado em java, mas por convenção usa-se self.
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #adiciona o objeto criado na lista de restaurantes da classe Restaurante.
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}' #método para representar o objeto como string, útil para impressão, ele evita printar o local na memória.

    def listar_restaurantes(): 
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {"Ativo" if restaurante.ativo else "Desativado"}') #não usamos self aqui, porque o método não está relacionado a um objeto específico, mas sim à uma lista geral criada fora dos objetos.

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')

restaurante_pizza = Restaurante('Pizzaria Bella', 'Pizza')

Restaurante.listar_restaurantes()



#print(vars(restaurante_praca)) #vars() exibe os atributos do objeto em formato de dicionário, se não for usado, a impressão mostrará apenas o local na memória onde o objeto está armazenado.
#print(vars(restaurante_pizza))

#print(dir(restaurante_praca)) #dir() exibe todos os métodos possíveis e atributos do objeto.