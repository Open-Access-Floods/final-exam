import pandas as pd

# Definir o caminho do arquivo de entrada e saída
input_path = "Danos_Informados(2).csv"
output_path = "Danos_Informados_preparado.csv"

# 1. Ler o CSV ignorando as 4 primeiras linhas (metadados), com encoding Latin1 e delimitador ';'
df = pd.read_csv(input_path, skiprows=4, sep=';', encoding='latin-1')

# 2. Selecionar apenas as colunas desejadas
columns_to_keep = [
    "UF", "Município", "Registro", "Protocolo", "COBRADE", "Status", "População",
    "DH_Mortos", "DH_Feridos", "DH_Enfermos", "DH_Desabrigados", "DH_Desalojados",
    "DH_Desaparecidos", "DH_Outros Afetados"
]
df = df[columns_to_keep]

# 3. Substituir valores ausentes, vazios ou inválidos por 0
df = df.fillna(0)

# (Opcional) Garantir que colunas numéricas fiquem com tipo inteiro após substituir NaN por 0
numeric_cols = ["População", "DH_Mortos", "DH_Feridos", "DH_Enfermos", 
                "DH_Desabrigados", "DH_Desalojados", "DH_Desaparecidos", "DH_Outros Afetados"]
df[numeric_cols] = df[numeric_cols].astype(int)

# 4. Escrever o DataFrame resultante em um novo CSV com UTF-8 e vírgulas como separador
df.to_csv(output_path, sep=',', encoding='utf-8', index=False)

print(f"Arquivo de saída gerado: {output_path}")