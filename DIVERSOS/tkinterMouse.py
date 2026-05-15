#Exibindo as coordenadas do mouse em tempo real em uma janela usando Tkinter, e capturando a posição doscliques com o botão esquerdo do mouse.

import tkinter as tk

#Função que será chamada sempre que o mouse se mover dentro da janela. 
#Ela recebe um evento como argumento, que contém as coordenadas do mouse (event.x e event.y). 
# A função atualiza o texto do rótulo para mostrar as coordenadas atuais do mouse, X representando a coordenada horizontal e Y representando a coordenada vertical.
import tkinter as tk

# Função para atualizar coordenadas em tempo real
#event é uma ferramente tkinter que retorna eventos ocorridos na janela, como movimento do mouse ou clique.
def atualizar_coordenadas(event):
    x = event.x 
    y = event.y

    label_mouse.config(
        text=f"Coordenadas do mouse em tempo real -> X={x} | Y={y}"
    )

# Função para capturar clique, que é chamada quando o usuário clica com o botão esquerdo do mouse.
def capturar_clique(event):
    x = event.x
    y = event.y

    # Insere o texto no final da caixa
    #Caixa_texto é a váriavel que vai receber o texto, e o método insert é usado para adicionar o texto na caixa de texto.  
    #tk.END é uma constante que representa o final do conteúdo da caixa de texto, garantindo que o novo texto seja adicionado ao final da caixa.
    caixa_texto.insert(
        tk.END,
        f"Último clique -> X={x} | Y={y}\n"
    )

    # Faz a rolagem automática para o final
    caixa_texto.see(tk.END) #O método see é usado para garantir que a caixa de texto role automaticamente para mostrar o último texto inserido, ou seja, o último clique capturado.

# Janela principal

janela = tk.Tk()
janela.title("Coordenadas do Mouse")
janela.geometry("700x400")

# Label das coordenadas em tempo real
label_mouse = tk.Label(
    janela,
    text="Mova o mouse...",
    font=("Arial", 14)
)

label_mouse.pack(pady=20)

# Caixa de texto copiável
caixa_texto = tk.Text( #tk.Text é um widget do Tkinter que permite criar uma caixa de texto multilinha, onde os usuários podem inserir ou copiar texto.
    janela,
    width=50,
    height=10,
    font=("Consolas", 12)
)

caixa_texto.pack(pady=20)

# #O método bind é usado para associar um evento a uma função.
janela.bind("<Motion>", atualizar_coordenadas) #<Motion> é o evento que ocorre quando o mouse se move dentro da janela, e atualizar_coordenadas é a função que será chamada para atualizar as coordenadas em tempo real.
janela.bind("<Button-1>", capturar_clique) #<Button-1> é o evento que ocorre quando o usuário clica com o botão esquerdo do mouse, e capturar_clique é a função que será chamada para capturar as coordenadas do clique e exibi-las na caixa de texto.

# Loop principal
janela.mainloop()