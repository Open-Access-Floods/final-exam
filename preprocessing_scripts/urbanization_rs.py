import pandas as pd

# Caminho do arquivo original
file_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_pre_processed/urbanization_growth_by_mun.csv"

# Caminho do arquivo de saída
output_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/urbanization_growth_rs.csv"

# Carrega o CSV
df = pd.read_csv(file_path)

# Filtra apenas os municípios do Rio Grande do Sul
df_rs = df[df["state"] == "Rio Grande do Sul"]

# Salva o novo CSV
df_rs.to_csv(output_path, index=False)

print("✅ Arquivo filtrado salvo com sucesso!")