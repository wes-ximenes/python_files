# Utilizando a API do WeatherAPI para obter dados meteorológicos
# Uma API (Application Programming Interface) é uma ponte que permite seu código solicitar dados de algum software externo, como um serviço web.

import requests #biblioteca requests é usada para fazer requisições HTTP em Python, facilitando a comunicação com APIs web.
import pprint #biblioteca pprint (pretty print) é usada para imprimir dados de forma mais legível, especialmente útil para estruturas de dados complexas como dicionários e listas aninhadas.

api_key = "975c3d4166424d66b0a124523252912" # Se consegue a chave de API ao se cadastrar no site do serviço, geralmente é gratuita para uso básico.

api_url = "http://api.weatherapi.com/v1/current.json" #Endereço de onde a API está hospedada, local onde as requisições serão enviadas, geralmente estão em JSON ou XML.

parametros = { #Para toda requisição existem parâmetros que devem ser enviados em formato de dicionário, para que a API entenda o que você está solicitando.
    "key": api_key, #Parâmetro obrigatório para autenticação.
    "q": "Paris", #Parâmetro 'q' indica a localização para a qual queremos obter os dados meteorológicos, 'q' vem de 'query' (consulta).
    "lang": "pt", #Parâmetro opcional que define o idioma da resposta, vem de 'language' (idioma).
}

resposta = requests.get(api_url, params=parametros) #Faz a requisição GET para a API, enviando os parâmetros definidos.

#print(resposta.status_code) 
#print(resposta.content) #Serve para ver o que está sendo retornado pela API, qual erro está acontecendo.

if resposta.status_code == 200: #Verifica se a requisição foi bem-sucedida (código 200 indica sucesso).
    dados = resposta.json() #Converte a resposta JSON em um dicionário Python.
    temperatura_celsius = dados['current']['temp_c'] #Acessa o valor da temperatura em Celsius no dicionário.
    condicao_tempo = dados['current']['condition']['text'] #Acessa a descrição da condição do tempo.
    data_atual = dados['location']['localtime'] #Acessa o horário local da localização consultada.
    print(f'Temperatura em {parametros["q"]}: {temperatura_celsius}°C') #A localização vai ser a mesma que foi passada nos parâmetros.
    print(f'Condição: {condicao_tempo}')
    print(f'Data e hora local: {data_atual}')

    #pprint.pprint(dados) #pprint Imprime os dados de forma legível, ele organiza a estrutura do dicionário para facilitar a leitura, biblioteca que já vem embutida no Python.
    

'''
código de status HTTP da resposta, 200 indica sucesso.
Códigos comuns:
#200 - OK (requisição bem-sucedida)
#300 - Multiple Choices (redirecionamento, significa que sua requisição foi redirecionada para outro endpoint)
#400 - Bad Request (requisição inválida)
#401 - Unauthorized (não autorizado, chave inválida, você deve se autenticar)
#403 - Forbidden (proibido, acesso negado)
#404 - Not Found (não encontrado, endpoint inválido)
#500 - Internal Server Error (erro interno do servidor, não é um erro do seu código, o sistema API está com problemas)
'''