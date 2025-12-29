class Restaurante: #classe funciona como um molde para criar objetos

    restaurantes = []

    def __init__(self, nome, categoria): # init serve para inicializar os atributos do objeto, muito usado em classes/ self representa o objeto que está sendo criado, pode ser substituído por qualquer outro nome, como "this", usado em java, mas por convenção usa-se self.
        self._nome = nome.title() #método title() coloca a primeira letra de cada palavra em maiúsculo.
        self.categoria = categoria.title()
        self._ativo = False #atributo privado, por convenção, atributos privados são precedidos por um underline (_), indicando que não devem ser acessados diretamente fora da classe.
        Restaurante.restaurantes.append(self) #adiciona o objeto criado na lista de restaurantes da classe Restaurante.
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}' #método para representar o objeto como string, útil para impressão, ele evita printar o local na memória.

    def listar_restaurantes(): 
        print(f'{"Nome:".ljust(25)} | {"Categoria:".ljust(25)} | Status:')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {"Ativo" if restaurante.ativo else "Desativado"}') #não usamos self aqui, porque o método não está relacionado a um objeto específico, mas sim à uma lista geral criada fora dos objetos.

    @property #decorador que serve para transformar o método em um atributo, para que não mexam no valor do atributo da classe diretamente, se for fazer alguma alteração, deve se criar um setter.
    #apenas necessário quando se quer proteger o atributo de alterações diretas. Quando você notar que esse atributo precisa de alguma validação ou lógica ao ser acessado.
    def ativo(self): #método para ativar o restaurante 
        return self._ativo #retorna o valor do atributo privado _ativo.
    
    @ativo.setter #decorador que indica que o método abaixo é um setter, usado para definir o valor do atributo protegido.
    def ativo(self, valor):
        if isinstance(valor, bool): #verifica se o valor passado é do tipo booleano.
            self._ativo = valor #se for booleano, atribui o valor ao atributo privado _ativo.
        else:
            raise ValueError('O valor deve ser True ou False') #se não for booleano, lança um erro.
        
    def alternar_status(self): #método para alternar o status do restaurante entre ativo e desativado.
        self._ativo = not self._ativo #not inverte o valor do atributo _ativo.    

restaurante_praca = Restaurante('restaurante da Praça', 'Comida Caseira')
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('pizzaria Bella', 'Pizza')

Restaurante.listar_restaurantes()



#print(vars(restaurante_praca)) #vars() exibe os atributos do objeto em formato de dicionário, se não for usado, a impressão mostrará apenas o local na memória onde o objeto está armazenado.
#print(vars(restaurante_pizza))

#print(dir(restaurante_praca)) #dir() exibe todos os métodos possíveis e atributos do objeto.