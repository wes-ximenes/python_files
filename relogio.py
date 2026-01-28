#Relógio criado para auxiliar nos estudos.

import tkinter as tk #biblioteca tkinter é padrão do python, serve para criar interfaces gráficas.
from time import strftime #strftime é uma classe da biblioteca time, que serve para formatar data e hora como string, ela usa as infos de data e hora do sistema operacional.

def atualizar_relogio(): 
    hora = strftime('%H:%M:%S') # %H = hora em formato 24h, %M = minutos, %S = segundos
    data = strftime('%d/%m/%Y') # %d = dia, %m = mês, %Y = ano com 4 dígitos
    dia_semana = strftime('%A') # %A = dia da semana por extenso

    label_hora.config(text=hora) #label é um WIDGET do tkinter que serve para exibir texto na tela. O método .config() permite alterar as propriedades do widget, nesse caso estamos alterando o texto exibido.
    label_data.config(text=f"{dia_semana} | {data}") #f-string para formatar a string exibida no label_data.

    label_hora.after(1000, atualizar_relogio) 
    #O método .after() do tkinter agenda a execução de uma função após um determinado tempo (em milissegundos).
    #Ele fará isso num looping infinito, atualizando o relógio a cada 1000 milissegundos (1 segundo).

janela = tk.Tk() # tk.Tk() serve para criar a janela principal da aplicação.
janela.title("Relógio Wesley") # Define o título da janela.

janela.state('zoomed') # Abre a janela em modo maximizado, se não utilizar esse método, a janela abrirá sem opção de maximizar.

janela.configure(bg="black") # Configura a cor de fundo da janela para preto, bg = background.

fonte_hora = ("Arial", 100, "bold") # Define a fonte para o horário exibido, com tamanho 100 e negrito.
fonte_data = ("Arial", 30)

label_hora = tk.Label(#tk.label configura os textos(rótulos) que serão exibidos na janela.
    janela, #janela criada anteriormente com tk.Tk()
    font=fonte_hora,
    bg="black", #background color
    fg="white" # Define a cor do texto para branco (fg = foreground)
)
label_hora.pack(expand=True) #O método .pack() organiza o widget na janela, expand=True faz com que o widget ocupe todo o espaço disponível, ajudando a centralizar.

label_data = tk.Label(#Mesma configuração do label_hora, mas para a data.
    janela,
    font=fonte_data,
    bg="black",
    fg="white"
)

label_data.pack(pady=20) #O método .pack() organiza o widget na janela, pady=20 adiciona um espaçamento vertical de 20 pixels entre os rótulos gerados na tela.

atualizar_relogio()
janela.mainloop() #O método .mainloop() inicia o loop principal da interface gráfica, mantendo a janela aberta e responsiva a eventos (como cliques e atualizações de tela).
