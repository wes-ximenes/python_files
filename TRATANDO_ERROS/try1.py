#try/except trata condições que podem gerar erros em tempo de execução, se ele encontrar um erro, ele não para o programa, mas sim executa o bloco 'except'.
#Nesse exemplo, usamos a classe genérica Exception para capturar qualquer tipo de erro que possa ocorrer, mas é possivel tratar erros específicos,
#como mostrado no arquivo tratandoErrosEspecif.py.

while True:
    try:  #tente executar esse bloco de código
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"O resultado da divisão é: {resultado:.1f}")

    except Exception as erro:  #se ocorrer algum erro, execute esse bloco (exception é uma classe genérica para capturar qualquer tipo de erro).
        print(f"Ocorreu um erro {erro.__class__}! Verifique os dados e tente novamente.")

    else:  #se não ocorrer nenhum erro, execute esse bloco (tambem é possivel usar o else, para exibir uma mensagem de sucesso, esse bloco é opcional).
        print("Divisão realizada com sucesso!")
        break  #se tudo ocorrer bem, saia do loop

    finally:  #esse bloco é sempre executado, independente se houve erro ou não (tambem é opcional).
        print("Finalizado.")