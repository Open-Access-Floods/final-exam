import pandas as pd

# Carrega os dados do S2ID
df = pd.read_csv("data_pre_processed/s2id_eventos_2024.csv")

# Colunas de pessoas afetadas
colunas_afetados = [
    "deaths", "injured", "sick", "displaced",
    "homeless", "disapeared", "other affecteds"
]

# Preencher nulos
df[colunas_afetados] = df[colunas_afetados].fillna(0)

# Total afetados por linha
df["total_afetados"] = df[colunas_afetados].sum(axis=1)

# 🧽 Normalização: tira espaços extras, mantém acentos, corrige capitalização
df["municipality"] = df["municipality"].astype(str).str.strip().str.title()
df["state"] = df["state"].astype(str).str.strip().str.upper()  # sigla UF fica em maiúsculo mesmo

# Agrupa mantendo colunas separadas
df_resumo = df.groupby(["municipality", "state"]).agg(
    total_eventos=("register", "count"),
    total_afetados=("total_afetados", "sum"),
    populacao_total=("population", "max")
).reset_index()

# Percentual
df_resumo["percentual_afetados"] = (
    df_resumo["total_afetados"] / df_resumo["populacao_total"]
) * 100

# Exporta
df_resumo.to_csv("s2id_resumo_municipio_estado_2024.csv", index=False)

print("✅ Arquivo final salvo com nomes normalizados e colunas separadas.")
