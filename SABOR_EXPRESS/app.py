#utilizar funções em todo o código, ajuda a organizar melhor o código e facilitar a leitura, ficando mais limpo.

import os #biblioteca para interações com o sistema operacional, contendo alguns comandos como limpar o terminal os.system("cls").

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
    4 - Sair do sistema
        
        """)

def encerrar_app():
    os.system("cls")
    print("Encerrando o Sabor Express... \nAté a próxima!")

def escolher_opcao():
    while True:

        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in [1, 2, 3, 4]:
                break
            else:
                os.system("cls")
                print("Opção inválida! Por favor, digite um número de 1 a 4.\n") #esse else trata se caso o usuário digite um número fora do intervalo esperado.

        except ValueError:
            os.system("cls")
            print("Opção inválida! Por favor, digite um número de 1 a 4.\n") #esse except trata se caso o usuário digite um valor que não seja numérico.

    if opcao == 1:
        os.system("cls")
        print("Você escolheu a opção de cadastrar restaurante.\n")
        #adicionar a lógica para cadastrar um restaurante       

    elif opcao == 2:
        os.system("cls")
        print("Você escolheu a opção de listar restaurantes.\n")
        #adicionar a lógica para listar restaurantes

    elif opcao == 3:
        os.system("cls")
        print("Você escolheu a opção de ativar/desativar restaurante.\n")
        #adicionar a lógica para ativar/desativar restaurante

    else:
        encerrar_app()    

def main():
    os.system("cls")
    nome_app()
    menu_app()
    escolher_opcao()  

if __name__ == "__main__": #declaramos que o arquivo app.py é o arquivo principal, então se "app.py" for executado, a função main() será chamada automaticamente.
    main()   



