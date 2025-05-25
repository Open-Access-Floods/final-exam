import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Caminhos
csv_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_pre_processed/precipitacao_mensal_estacoes_rs.csv"
shp_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/RG2017_rgint_20180911"  # pasta com o shapefile
output_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/precip_rs_por_regiao_intermediaria.csv"

# 1. Ler CSV de chuvas
df = pd.read_csv(csv_path)
print("📋 Colunas disponíveis:", df.columns.tolist())

# 2. Criar GeoDataFrame com pontos
gdf_estacoes = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
    crs="EPSG:4326"
)

# 3. Ler shapefile das regiões intermediárias
gdf_rgint = gpd.read_file(shp_path)

# 4. Garantir mesmo CRS
gdf_rgint = gdf_rgint.to_crs("EPSG:4326")

# 5. Spatial Join
gdf_joined = gpd.sjoin(gdf_estacoes, gdf_rgint, how="left", predicate="within")

# 6. Agregar por nome da região e mês
df_final = gdf_joined.groupby(["NM_RGINT", "AnoMes"])["Precipitacao"].sum().reset_index()

# 7. Salvar CSV
df_final.to_csv(output_path, index=False)

print("✅ CSV salvo com sucesso!")
