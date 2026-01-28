#A função open() em python é usada para abrir arquivos e realizar operações de leitura ou escrita neles.
#nesse exemplo criamos um arquivo txt, escrevemos algumas linhas nele e depois lemos o conteúdo do arquivo e imprimimos na tela.
#também é possível usar o open() para manipular outros tipos de arquivos, como arquivos CSV, JSON, entre outros.

with open ('infos.txt', 'w') as arquivo: #criando o arquivo infos.txt em modo de escrita ('w' = write)
    arquivo.write('Linha 1: Olá, mundo!\n')
    arquivo.write('Linha 2: Utilizando a função open em Python.\n')
    arquivo.write('Linha 3: Manipulação de arquivos com open.\n')

with open ('infos.txt', 'r') as arquivo: #lendo o arquivo infos.txt em modo de leitura ('r' = read)
    conteudo = arquivo.read() #lendo todo o conteúdo do arquivo e armazenando na variável conteudo
    print(conteudo)

with open ('infos.txt', 'a') as arquivo: #abrindo o arquivo infos.txt em modo de adição ('a' = append)
    arquivo.write('Linha 4: Adicionando uma nova linha ao arquivo.\n')
    
with open ('infos.txt', 'r') as arquivo: #lendo o arquivo infos.txt novamente para ver o conteúdo atualizado
    conteudo = arquivo.read()
    print(conteudo)