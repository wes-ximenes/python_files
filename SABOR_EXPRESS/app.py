#utilizar funções em todo o código, ajuda a organizar melhor o código e facilitar a leitura, ficando mais limpo e fácil de corrigir algum bug.

import os #biblioteca para interações com o sistema operacional, contendo alguns comandos como limpar o terminal "os.system("cls")".

restaurantes = [{'nome': 'Umi', 'categoria': 'Japonesa','ativo': True}, 
                {'nome': 'Burger House', 'categoria': 'Hamburgueria','ativo': False}, 
                {'nome': 'Pasta Bella', 'categoria': 'Massas','ativo': False},
                {'nome': 'Taco Loco', 'categoria': 'Mexicana','ativo': True}
                ] #lista de dicionários para armazenar os restaurantes cadastrados, com dicionários se torna mais fácil manipular os dados.

def nome_app():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def menu_app():
    print("""
    Bem-vindo ao Sabor Express!
        
    Escolha uma das opções abaixo para continuar:
        
    1 - Cadastrar restaurante
    2 - Listar restaurantes
    3 - Ativar/Desativar restaurante
    4 - Apagar restaurante cadastrado      
    5 - Sair do sistema
        
        """)

def encerrar_app():
    os.system("cls")
    print("Encerrando o Sabor Express... \nAté a próxima!")

def voltar_menu():
    input("Pressione enter, para voltar ao menu principal...")
    main()

def cadastrar_restaurante():
    '''Função para cadastrar um novo restaurante.
    inputs: nome e categoria do restaurante.
    outputs: adiciona o restaurante à lista de restaurantes.
    '''
    os.system("cls")
    print("CADASTRO DE RESTAURANTES\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante} (Tipo de refeição servida): ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f"\nRestaurante '{nome_restaurante}' cadastrado com sucesso!\n")
    voltar_menu()

def exibir_subtitulo(texto):
    '''Função para exibir subtítulos formatados'''

    os.system("cls")
    linha_de_asteriscos = '*' * len(texto)
    print(linha_de_asteriscos)
    print(texto)
    print(linha_de_asteriscos)
    print()

def listar_restaurantes():
    '''Função para listar todos os restaurantes cadastrados.

<<<<<<< HEAD
    Percorre a lista de restaurantes com laço 'for' e exibe o nome, categoria e status de cada um.
=======
    Percorre a lista de restaurantes com 'for' e exibe o nome, categoria e status de cada um.
>>>>>>> 06bcc001f2da7df844d6b8c2fb56b3f04884b406

    outputs: exibe no terminal a lista de restaurantes com nome, categoria e status.
    '''

    os.system("cls")
    exibir_subtitulo("LISTA DE RESTAURANTES CADASTRADOS")
    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria restaurante:'.ljust(31)} | Status:\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        print(f"- {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Ativo: {'Sim' if restaurante['ativo'] else 'Não'}\n")
        #É possivel usar condicionais dentro das f-strings.
        #ljust() alinha o texto à esquerda, e o número dentro do parênteses define os espaços reservados.
    voltar_menu()

def alternar_status ():
    '''Função para ativar ou desativar um restaurante.
    inputs: busca o nome do restaurante.
    outputs: altera o status do restaurante na lista de restaurantes utilizando o not
    '''

    exibir_subtitulo("ATIVAR/DESATIVAR RESTAURANTE")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower(): #usamos .lower() para ignorar diferenças entre maiúsculas e minúsculas.
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #not inverte o valor booleano, se for True vira False e vice-versa.
            status = 'ativado' if restaurante['ativo'] else 'desativado' #criada uma variável temporária para armazenar o status atual do restaurante, usando ternário.
            print(f"\nRestaurante '{nome_restaurante}' foi {status} com sucesso!\n") 
            break #usamos break para sair do loop assim que o restaurante for encontrado.
    if not restaurante_encontrado: #se o restaurante_encontrado não for alterado para True, então o restaurante não foi encontrado.
        print(f"\nRestaurante '{nome_restaurante}' não encontrado na lista de cadastrados.\n")

    voltar_menu()

def apagar_restaurante():
    '''
    Função para apagar um restaurante da lista.
    inputs: busca o nome do restaurante.
    outputs: remove o restaurante da lista de restaurantes.
    '''
    exibir_subtitulo('APAGAR RESTAURANTE')
    nome_restaurante = input("Digite o nome do restaurante que deseja apagar: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurantes.remove(restaurante) #remove o restaurante da lista.
            print(f"\nRestaurante '{nome_restaurante}' foi apagado com sucesso!\n")
            break

    if not restaurante_encontrado:
        print(f"\nRestaurante '{nome_restaurante}' não encontrado na lista de cadastrados.\n")

    voltar_menu()

def escolher_opcao():
    '''Função para escolher a opção do menu.
    inputs: opção escolhida pelo usuário.
    outputs: chama a função correspondente à opção escolhida.
    '''

    while True:

        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in [1, 2, 3, 4, 5]:
                break
            else:
                os.system("cls")
                print("Opção inválida! Por favor, digite um número de 1 a 4.\n") #esse else trata se caso o usuário digite um número fora do intervalo esperado.

        except ValueError:
            os.system("cls")
            print("Opção inválida! Por favor, digite um número de 1 a 4.\n") #esse except trata se caso o usuário digite um valor que não seja numérico.

    if opcao == 1:
        cadastrar_restaurante()

    elif opcao == 2:
        listar_restaurantes()

    elif opcao == 3:
        os.system("cls")
        alternar_status ()

    elif opcao == 4:
        os.system("cls")
        apagar_restaurante()
       
    else:
        encerrar_app()    

def main():
    '''Função principal do aplicativo.
    Chama as funções para exibir o nome do app, o menu e escolher a opção.
    '''

    os.system("cls")
    nome_app()
    menu_app()
    escolher_opcao()  

if __name__ == "__main__": #declaramos que o arquivo app.py é o arquivo principal, então se "app.py" for executado no terminal, a função main() será chamada automaticamente.
    main()   



