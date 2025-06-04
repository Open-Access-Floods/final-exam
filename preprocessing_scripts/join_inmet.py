import pandas as pd
from pathlib import Path

# Caminho da pasta onde estão os CSVs
pasta_csv = Path("/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/inmet2024")

# Lista todos os arquivos .CSV da pasta
arquivos = list(pasta_csv.glob("*.CSV"))

# Lista para guardar os DataFrames
chuvas = []

# Iterar sobre todos os arquivos
for arquivo in arquivos:
    try:
        df = pd.read_csv(arquivo, sep=";", encoding="latin1", skiprows=8)
        df = df[["Data", "Hora UTC", "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"]]
        df["arquivo"] = arquivo.name
        chuvas.append(df)
    except Exception as e:
        print(f"Erro ao processar {arquivo.name}: {e}")

# Concatenar tudo em um único DataFrame
df_final = pd.concat(chuvas, ignore_index=True)

# Salvar como CSV
output_path = pasta_csv.parent / "chuvas_com_arquivo.csv"
df_final.to_csv(output_path, index=False)

print(f"✅ Arquivo gerado em: {output_path}")