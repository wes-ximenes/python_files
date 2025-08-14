#Programa que analisa planilhas excel(nesse caso, está em formato libreoffice, então a formatação está em html) com base em data,
#e separa apenas os itens que estão com data de vencimento (30 dias) expiradas, dropando os itens repetidos e considerando os mais atuais.
import pandas as pd
from datetime import datetime

# Caminho do arquivo
caminho_arquivo = r"C:\Users\Wesley Ximenes\Downloads\relatorio fatura.xls"

# Lê todas as tabelas do arquivo
tabelas = pd.read_html(caminho_arquivo, decimal=",", thousands=".") #em html, pois o libre office tem esse formato, se não, usaria o read_excel
print(f"📊 {len(tabelas)} tabelas encontradas.")

# Seleciona a tabela correta (índice 1)
df = tabelas[1].copy()

# Usa a primeira linha como cabeçalho
df.columns = df.iloc[0]
df = df[1:].copy()
df.columns = df.columns.astype(str).str.strip()

# Verifica colunas essenciais
if 'placa' not in df.columns or 'dataentrada' not in df.columns:
    print("❌ Colunas 'placa' ou 'dataentrada' não encontradas.")
    print("🔍 Colunas disponíveis:", df.columns.tolist())
    exit()

# Limpa os dados
df['placa'] = df['placa'].astype(str).str.strip()
df['dataentrada'] = pd.to_datetime(df['dataentrada'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['placa', 'dataentrada'])

# Ordena por placa e dataentrada (mais recente primeiro)
df = df.sort_values(by=['placa', 'dataentrada'], ascending=[True, False])

# Remove duplicatas mantendo a data mais recente
df = df.drop_duplicates(subset='placa', keep='first')

# Calcula dias passados desde a data de entrada
hoje = datetime.now()
df['dias_passados'] = (hoje - df['dataentrada']).dt.days

# Filtra veículos com mais de 30 dias
vencidos = df[df['dias_passados'] > 30].sort_values(by='dias_passados', ascending=False)

# Exibe alerta
if not vencidos.empty:
    print("⚠️ Veículos com data de entrada vencida há mais de 30 dias:")
    print(vencidos[['placa', 'dataentrada', 'dias_passados']])

    # ✅ Salva os dados em um arquivo Excel com o openpyxl (biblioteca para trabalhar em arquivos excel)
    # Filtra apenas as colunas necessárias
    colunas_desejadas = ['placa', 'dataentrada', 'dias_passados']
    vencidos[colunas_desejadas].to_excel("veiculos_vencidos.xlsx", index=False)


else:
    print("✅ Nenhum veículo com data vencida encontrada.")
