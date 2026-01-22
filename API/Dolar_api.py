#API REST para cotação do Dólar.

import requests #primeiro importamos a biblioteca requests para fazer requisições HTTP.

url = "https://economia.awesomeapi.com.br/last/USD-BRL" #em seguida, alocamos a URL da API em uma variável. Essa URL retorna a cotação do Dólar em relação ao Real Brasileiro em formato JSON.

valor_dolar = requests.get(url) #usamos requests.get() para fazer uma requisição GET à URL da API. A informação buscada pela requisição é armazenado na variável valor_dolar.

dados_dolar = valor_dolar.json() #usamos o método .json() para converter as informações contidas em valor_dolar, num dicionário Python. Esse dicionário é armazenado na variável dados_dolar.

def cotacao_dolar(): #
    return float(dados_dolar['USDBRL']['bid']) #definimos a função cotacao_dolar() que retorna a cotação atual do Dólar em relação ao Real. A cotação é obtida acessando o dicionário dados_dolar, especificamente o valor associado à chave 'bid' dentro do dicionário 'USDBRL'. Esse valor é convertido para float antes de ser retornado.

print(f'Cotação do Dólar ({dados_dolar["USDBRL"]["create_date"]}): R$ {cotacao_dolar():.2f}') #Exibindo o resultado da cotação do Dólar formatada com duas casas decimais, juntamente com a data e hora da última atualização da cotação, que é obtida a partir do dicionário dados_dolar.