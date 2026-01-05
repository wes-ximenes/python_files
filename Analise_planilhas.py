#Programa que analisa planilhas excel com pandas, lxml e openpyxl(nesse caso, a planilha foi feita em libreoffice, então a formatação está em html) com base em data,
#e separa apenas os itens que estão com data de vencimento (30 dias) expiradas, dropando os itens repetidos e considerando os mais atuais.
import pandas as pd
from datetime import datetime

# Caminho do arquivo
caminho_arquivo = r"C:\Users\Wesley Ximenes\Downloads\relatorio fatura.xls" #'r' indica que é uma raw string, para evitar conflitos com barras invertidas.

# Lê todas as tabelas do arquivo
tabelas = pd.read_html(caminho_arquivo, decimal=",", thousands=".") #em html, pois o libre office tem esse formato, se não, usaria o read_excel

# Seleciona a tabela correta (índice 1)
df = tabelas[1].copy() #Seleciona a segunda tabela (o indice 1), contendo as infos dos veículos / o copy evita alterações acidentais ta tabela original.

# Usa a primeira linha como cabeçalho
df.columns = df.iloc[0] #indexador do pandas, define a primeira linha da tabela como os nomes das colunas
df = df[1:].copy() #remove essa linha dos dados, para que ela não seja analisada junto.
df.columns = df.columns.astype(str).str.strip() #garante que os nomes das colunas fiquem strings limpas, sem espaços (strip).

# Verifica colunas essenciais, se não estiverem presentes, retorna uma msg de erro e encerra o programa.
if 'placa' not in df.columns or 'dataentrada' not in df.columns:
    print("Colunas 'placa' ou 'dataentrada' não encontradas.")
    print("Colunas disponíveis:", df.columns.tolist())
    exit()

# Limpa os dados
df['placa'] = df['placa'].astype(str).str.strip() #converte as coluna 'placa' para string e remove possíveis espaços com o strip.
df['dataentrada'] = pd.to_datetime(df['dataentrada'], dayfirst=True, errors='coerce') #converte 'dataentrada' para formato datetime, tratando erros com 'coerce', datas inválidas viram NaT(nota a time).
df = df.dropna(subset=['placa', 'dataentrada']) #Remove linhas onde 'placa' ou 'dataentrada' estão ausentes.

# Ordena por placa e dataentrada (mais recente primeiro)
df = df.sort_values(by=['placa', 'dataentrada'], ascending=[True, False]) #Ordena os dados por 'placa'(a-z) e 'dataentrada'(mais recentes primeiro).

# Remove duplicatas mantendo a data mais recente
df = df.drop_duplicates(subset='placa', keep='first')

# Calcula dias passados desde a data de entrada
hoje = datetime.now()
df['dias_passados'] = (hoje - df['dataentrada']).dt.days #Cria uma nova coluna 'dias_passados' com esse valor.

# Filtra veículos com mais de 30 dias
vencidos = df[df['dias_passados'] > 30].sort_values(by='dias_passados', ascending=False) #Coloca os vencidos em ordem decrescente (ascending=false)

if not vencidos.empty: #Se houver veículos vencidos: Exibe os dados filtrados no terminal e salva apenas as colunas relevantes num excel.
    print("⚠️ Veículos com data de entrada vencida há mais de 30 dias:")
    print(vencidos[['placa', 'dataentrada', 'dias_passados']])

    colunas_desejadas = ['placa', 'dataentrada', 'dias_passados'] #Filtra apenas as colunas necessárias 
    vencidos[colunas_desejadas].to_excel("veiculos_vencidos.xlsx", index=False) #Salva os dados em um arquivo Excel com o openpyxl (biblioteca para trabalhar em arquivos excel)

else: #Se não houver veículos vencidos, retorna a msg positiva.
    print("✅ Nenhum veículo com data vencida encontrada.")
