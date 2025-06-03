op = ''
result = ''
while op != '5':
    op = input('\n[1] Soma\n[2] Subtração\n[3] Muliplicação\n[4] Divisão\n[5] Sair\n\n ')
    if op == '5':
        print('Fim da execução da calculadora')
        break
    n1 = int(input('1º número: '))
    n2 = int(input('2º número: '))

    if op == '1':
        result = n1 + n2
    elif op == '2':
        result = n1 - n2
    elif op == '3':
        result = n1 * n2
    elif op == '4':
        result = n1 / n2
    else:
        print("❌ Opção inválida.")
        continue                    
    print(f'\nResultado: {result}')
    
    
