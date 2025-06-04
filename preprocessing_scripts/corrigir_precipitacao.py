import pandas as pd
from pathlib import Path

# Caminho do arquivo original
input_path = Path("/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/chuvas_com_arquivo.csv")
output_path = input_path.parent / "chuvas_corrigido.csv"

# Ler CSV
df = pd.read_csv(input_path)

# Corrigir coluna de precipitação
def normalizar_precipitacao(val):
    try:
        val = str(val).strip().replace(",", ".")
        return float(val)
    except:
        return None  # ou 0 se quiser preencher com zero

df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"] = df["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"].apply(normalizar_precipitacao)

# Salvar resultado
df.to_csv(output_path, index=False)

print(f"✅ Arquivo corrigido salvo em: {output_path}")
