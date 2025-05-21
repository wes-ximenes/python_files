import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\n📛 Nome: {dados['name'].capitalize()}")
        print(f"🆔 ID: {dados['id']}")
        print("🧬 Tipos:")
        for tipo in dados['types']:
            print(f" - {tipo['type']['name'].capitalize()}")
        print(f"⚖️ Peso: {dados['weight'] / 10} kg")
        print(f"📏 Altura: {dados['height'] / 10} m")
    else:
        print("❌ Pokémon não encontrado.")

# Loop interativo
while True:
    nome = input("\nDigite o nome do Pokémon (ou 'sair'): ")
    if nome.lower() == 'sair':
        break
    buscar_pokemon(nome)
