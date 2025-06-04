from pathlib import Path
import pandas as pd

# 👇 Altere para o caminho real da sua pasta
inmet_dir = Path("/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/inmet2024")

# Função para extrair os metadados
def extrair_metadados_do_arquivo(caminho_csv):
    try:
        with open(caminho_csv, 'r', encoding='latin1') as f:
            linhas = [next(f).strip() for _ in range(8)]
        dados = {linha.split(":;")[0]: linha.split(":;")[1] for linha in linhas if ":;" in linha}
        return {
            "arquivo": caminho_csv.name,
            "estacao": dados.get("ESTACAO", ""),
            "uf": dados.get("UF", ""),
            "latitude": dados.get("LATITUDE", "").replace(",", "."),
            "longitude": dados.get("LONGITUDE", "").replace(",", ".")
        }
    except Exception as e:
        return {"arquivo": caminho_csv.name, "erro": str(e)}

# Ler todos os arquivos da pasta
todos_csvs = list(inmet_dir.glob("*.CSV"))
metadados_extraidos = [extrair_metadados_do_arquivo(f) for f in todos_csvs]

# Criar DataFrame e salvar
df_meta = pd.DataFrame(metadados_extraidos)

# ✅ Garante que a pasta de destino exista
output_dir = inmet_dir.parent  # mesma pasta "final-exam"
output_path = output_dir / "metadados_estacoes.csv"
df_meta.to_csv(output_path, index=False)

print(f"✅ Metadados salvos em: {output_path}")