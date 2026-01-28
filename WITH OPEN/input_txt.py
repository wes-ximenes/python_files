# Coleta informações do usuário e as salva em um arquivo txt.

while True:
    nome = input('Digite seu nome: ')
    if nome.lower() == 'sair':
        break
    idade = input('Digite sua idade: ')
    if idade.lower() == 'sair':
        break
    estado_civil = input('Digite seu estado civil: ')
    if estado_civil.lower() == 'sair':
        break

    #O open com 'w' cria um novo arquivo ou sobrescreve o existente. Após a primeira vez, usar 'a' para adicionar sem apagar o conteúdo anterior no .txt
    # with open('dados_usuario.txt', 'w', encoding='utf-8') as arquivo: # 'w' = write, cria um novo arquivo ou sobrescreve o existente.
    #     arquivo.write(f'Nome: {nome}\n')
    #     arquivo.write(f'Idade: {idade}\n')
    #     arquivo.write(f'Estado Civil: {estado_civil}\n')

    with open('dados_usuario.txt', 'a', encoding='utf-8') as arquivo: # 'a' = append, adiciona ao final do arquivo sem apagar o conteúdo anterior. encoding='utf-8' para suportar caracteres especiais.
        arquivo.write(f'Nome: {nome.title()}\n')
        arquivo.write(f'Idade: {idade}\n')
        arquivo.write(f'Estado Civil: {estado_civil.title()}\n\n') # \n\n Adiciona uma linha em branco entre os registros

