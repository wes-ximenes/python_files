#TKINTER é uma Biblioteca para criar interfaces gráficas
#Ela é uma biblioteca padrão do Python, ou seja, não é necessário instalá-la para utilizá-la.
#Com o Tkinter, é possível criar janelas, botões, rótulos, caixas de texto, entre outros elementos gráficos para criar aplicações desktop.

from tkinter import *

janelaPrincipal = Tk() #Criando a janela principal da aplicação, onde serão adicionados os elementos gráficos.

texto = Label(master = janelaPrincipal, text = "Minha janela exibida") #Criando um rótulo (Label) com o texto "Minha janela exibida" e associando-o à janela principal (master = janelaPrincipal).
texto.place(x = 50, y = 100) #Place é um método que posiciona o elemento gráfico na janela, onde x é a coordenada horizontal e y é a coordenada vertical.
janelaPrincipal.mainloop() #Iniciando o loop principal da aplicação, que mantém a janela

