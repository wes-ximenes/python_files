# Percorrendo um dicionário com for:

filmes = {
    "Circulo de fogo": "Ficção Científica",
    "Crepusculo": "Romance",
    "Interestelar": "Ficção Científica",
    "Minha mãe é uma peça": "Comédia"
}

for filme, genero in filmes.items(): #Para percorrer um dicionário, chamamos dois parâmetros na estrutura de repetição: chave e valor (filme e gênero, nesse caso).
#Diferente de listas e tuplas, para percorrer dicionários usamos o método .items() para obter tanto a chave quanto o valor.    
    print(f'O filme {filme} é do gênero {genero}.')