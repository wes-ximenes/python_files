import requests #biblioteca que permite voce acessar infos na nuvem, como por exemplo essa API usada 'PokeAPI'

def buscar_pokemon(nome): #Define uma função, 'buscar_pokemon' e o nome que voce digitar
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}" #Criando a url da API, padronizando o nome digitado em minusculo para evitar erro na API
<<<<<<< HEAD
    resposta = requests.get(url) #faz uma requisição HTTP GET a URL e a 'resposta' vai armazenar as infos que a API desenvolver perante sua busca.

=======

    resposta = requests.get(url) #faz uma requisição HTTP GET a URL e a 'resposta' vai armazenar as infos que a API desenvolver perante sua busca.

>>>>>>> da2d33e (update new python files)
    if resposta.status_code == 200: #Código 200 é o cod que deu tudo certo (cod 404 = erro)
        dados = resposta.json() #Converte os dados em json (dados estruturados, como um dicionário)
        print(f"\n📛 Nome: {dados['name'].capitalize()}")
        print(f"🆔 ID: {dados['id']}")
        print("🧬 Tipos:")
        for tipo in dados['types']: #'Tipo' é o unico dado que possui uma lista de tipos (fogo, agua, etc), e o 'for' faz ele acessar a lista de tipos para buscar o dado.
            print(f" - {tipo['type']['name'].capitalize()}")
        print(f"⚖️ Peso: {dados['weight'] / 10} kg")
        print(f"📏 Altura: {dados['height'] / 10} m")
    else:
        print("❌ Pokémon não encontrado.")

# Loop interativo
while True: #Vai ficar pedindo um novo nome de busca até vc digitar 'sair'.
    nome = input("\nDigite o nome do Pokémon (ou 'sair'): ")
    if nome.lower() == 'sair':
        break
    buscar_pokemon(nome) #Necessário chamar a função sempre que houver um 'input', para leitura e execução do input.
