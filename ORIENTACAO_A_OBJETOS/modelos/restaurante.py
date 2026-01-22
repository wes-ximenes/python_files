from .avaliacoes import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante: #classe funciona como um molde para criar objetos

    restaurantes = []

    def __init__(self, nome, categoria): # init serve para inicializar os atributos do objeto, muito usado em classes/ self representa o objeto que está sendo criado, pode ser substituído por qualquer outro nome, como "this", usado em java, mas por convenção usa-se self.
        self._nome = nome.title() #método title() coloca a primeira letra de cada palavra em maiúsculo.
        self.categoria = categoria.title()
        self._ativo = False #atributo privado, por convenção, atributos privados são precedidos por um underline (_), indicando que não devem ser acessados diretamente fora da classe.
        self._avaliacoes = [] #atributo privado para armazenar as avaliações do restaurante.
        self._cardapio = [] #atributo privado para armazenar os itens do cardápio do restaurante.
        Restaurante.restaurantes.append(self) #adiciona o objeto criado na lista de restaurantes da classe Restaurante.
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}' #método para representar o objeto como string, útil para impressão, ele evita printar o local na memória.

    @classmethod #decorador que indica que o método abaixo é um método de classe, ou seja, ele atua sobre a classe em si, e não sobre uma instância específica da classe.
    def listar_restaurantes(cls): 
        print(f'{"Nome:".ljust(25)} | {"Categoria:".ljust(25)} | {"Avaliação Média:".ljust(35)} | Status:')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(35)} | {"Ativo" if restaurante.ativo else "Desativado"}') #não usamos self aqui, porque o método não está relacionado a um objeto específico, mas sim à uma lista geral criada fora dos objetos.

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

    def adicionar_avaliacao(self, cliente, nota, comentario): #método para adicionar uma avaliação ao restaurante.
        if 0 < nota <= 5: #verifica se a nota está entre 0 e 5.
            avaliacao = Avaliacao(cliente, nota, comentario) #cria um objeto da classe Avaliacao, passando o restaurante atual (self), a nota e o comentário.
            self._avaliacoes.append(avaliacao) #adiciona a avaliação à lista de avaliações do restaurante.    

    @property #começa a tratar o 'média' como um atributo, para ser listado na listagem de restaurantes.
    def media_avaliacoes(self): #método para calcular a média das avaliações do restaurante.
        
        if not self._avaliacoes: #verifica se a lista de avaliações está vazia.
            return "Não avaliado, ou nota inválida" #se não houver notas, retorna essa mensagem.
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes) #pega todas as .nota da lista de avaliações e soma.
        numero_de_notas = len(self._avaliacoes) #vai pegar o comprimento da lista de avaliações (numero de notas contidas lá)  
        media = round(soma_das_notas / numero_de_notas, 1) #calcula a média e arredonda para 1 casa decimal.
        return media #retorna a média calculada. Na listagem vamos transformar a média em string para funcionar o ljust(), que só funciona com texto.
    
 
    def adicionar_ao_cardapio(self, item):
        if isinstance(item, ItemCardapio): #verifica se o item é uma instância da classe ItemCardapio ou suas subclasses (Prato, Bebida), pra adicionar precisa ter alguma ligação com ItemCardapio.
            self._cardapio.append(item)


    @property #property afirma que o método servirá apenas para leitura do atributo.
    def exibir_cardapio(self):
        if not self._cardapio:
            print("O cardápio está vazio.")
            return
        
        print(f'Cardápio do {self._nome}:\n')
        for i,item in enumerate(self._cardapio, start=1): #usando enumerate para pegar o índice e o item ao mesmo tempo. o 'i, item' representa o índice e o item respectivamente. start=1 faz a contagem começar do 1 ao invés do 0.
            if hasattr(item, 'descricao'): #hasattr (has atribute) verifica se o item tem o atributo 'descrição'.
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preço:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            
            elif hasattr(item, 'tamanho'): #verifica se o item tem o atributo 'tamanho'.
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preço:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)


        





#print(vars(restaurante_praca)) #vars() exibe os atributos do objeto em formato de dicionário, se não for usado, a impressão mostrará apenas o local na memória onde o objeto está armazenado.
#print(vars(restaurante_pizza))

#print(dir(restaurante_praca)) #dir() exibe todos os métodos possíveis e atributos do objeto.