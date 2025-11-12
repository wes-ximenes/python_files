# Tratando erros específicos

try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    resultado = a / b
    print(f"O resultado da divisão é: {resultado:.1f}")

except ValueError:  #se ocorrer um erro de valor, execute esse bloco.
    print("Erro: Você deve digitar números inteiros válidos")

except TypeError:  #se ocorrer um erro de tipo, execute esse bloco.
    print("Erro: Tipo de dado inválido para essa operação.")

except ZeroDivisionError:  #se ocorrer um erro de divisão por zero, execute esse bloco.
    print("Erro: Qualquer número dividido por zero, é indefinido.")

except KeyboardInterrupt:  #se o usuário interromper a execução do programa, execute esse bloco.
    print("\nErro: A execução do programa foi interrompida pelo usuário.")

else:
    print("Divisão realizada com sucesso!")
    