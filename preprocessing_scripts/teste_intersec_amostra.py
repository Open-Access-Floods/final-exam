import pandas as pd

# Caminho do seu arquivo
csv_estacoes = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/chuvas_com_arquivo.csv"

# Lê apenas o cabeçalho
df = pd.read_csv(csv_estacoes, nrows=5)

# Exibe as colunas
print("📋 Colunas disponíveis no arquivo de estações:")
print(df.columns)