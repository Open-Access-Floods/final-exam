import pandas as pd

# Caminhos dos arquivos
urban_file = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/urbanization_growth_rs.csv"
deforestation_file = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/mapbiomas_deflorestamento_extraido.csv"

# Carregar dados
df_urban = pd.read_csv(urban_file)
df_def = pd.read_csv(deforestation_file)

# Corrigir nomes para comparação
df_def['municipality'] = df_def['municipality'].str.upper()
df_urban['municipality'] = df_urban['municipality'].str.upper()

# Selecionar os 20 com maior área urbanizada em 2013
top20 = df_urban.sort_values(by="2013", ascending=False).head(20)

# Filtrar dados de desmatamento apenas para esses municípios e para "1.1. Forest Formation"
df_selected = df_def[
    (df_def['municipality'].isin(top20['municipality'])) &
    (df_def['class_level_2'] == '1.1. Forest Formation')
]

# Salvar o resultado
output_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/deforestation_top20_rs.csv"
df_selected.to_csv(output_path, index=False)

print("✅ Dados de desmatamento dos 20 maiores municípios salvos!")