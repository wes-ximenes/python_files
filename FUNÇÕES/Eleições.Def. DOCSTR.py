def voto(nasc):
    #DOCSTRING ABAIXO: Serve para documentar um código, caso alguem chame um "help(voto)", para saber oq ele faz.
    """
    VERIFICA SE UMA PESSOA PODE VOTAR COM BASE NO ANO DE NASCIMENTO DO INPUT
    
    PARÂMETROS:
    nasc(int): ano de nascimento da pessoa

    RETORNA:
    srt: uma msg indicando se o voto é NEGADO, OPCIONAL OU OBRIGATÓRIO
    """

    anoatual = 2025
    idade = anoatual - nasc

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    

nasc = int(input('Ano de nascimento: '))
print(voto(nasc))   

