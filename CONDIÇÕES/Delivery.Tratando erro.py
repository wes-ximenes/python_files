while True:
    try:
        valorCompra = float(input("Digite o valor da compra: R$ "))
        distancia = float(input("Digite a distância em km: "))
        chuva = input("Está chovendo? (s/n): ").lower()
        taxa = 0
        total = 0

        if distancia <= 5:
            taxa = 5.00
            if chuva == 's':
                taxa += 2.00
            total = valorCompra + taxa
            

        elif distancia > 5 and distancia <= 10:
            taxa = 8.00
            if chuva == 's':
                taxa += 2.00
            total = valorCompra + taxa

        else:
            taxa = 10.00 
            if chuva == 's':
                taxa += 2.00   
            total = valorCompra + taxa

        if chuva == 's':
            print (f'Total da compra: R$ {total:.2f} (Taxa de entrega: R$ {taxa:.2f} + adicional por chuva)')  

        else:
            print (f'Total da compra: R$ {total:.2f} (Taxa de entrega: R$ {taxa:.2f})')      

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}, tente novamente!", erro.__class__.__name__)
        

    sair = input("Deseja calcular outra entrega? (s/n): ").lower()
    if sair != 's':
        break    