# Exercício de Simulação de saque em um caixa eletrônico, que trata erros de entrada do usuário.

def caixa_eletronico(): 
    cedulas = [100, 50, 20, 10, 5, 2] 
 
    while True:
        try: 
            valor = int(input("Digite o valor do saque: ")) 
    
            if valor <= 0: 
                print("Erro: O valor deve ser positivo.")
            elif valor % 2 != 0: # para evitar que o usuário tente sacar um valor ímpar, já que a menor cédula disponível é de 2 reais
                print("Erro: O valor deve ser múltiplo de 2.") 
            else: 
                print("Cédulas entregues:")
                
                for cedula in cedulas: # percorre a lista de cédulas disponíveis
                    quantidade = valor // cedula # divisão inteira, para analisar quantas cédulas da lista cabem no valor do saque, sem valor quebrado. 
                    if quantidade > 0: #para evitar imprimir cédulas com quantidade zero
                        print(f"{quantidade} cédulas de R$ {cedula}")
                        valor = valor % cedula #verifica o valor que sobra após encaixar as cédulas maiores possíveis, e retorna o loop para analisar as próximas cédulas menores que ainda cabem.
                break  # Sai do loop se o saque for bem-sucedido             
    
        except ValueError: 
            print("Erro: Digite um valor numérico válido.") 
 
caixa_eletronico()