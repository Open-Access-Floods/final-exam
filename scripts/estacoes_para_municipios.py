import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Caminhos atualizados
csv_estacoes = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/metadados_estacoes.csv"  # seu novo CSV de metadados
shapefile_municipios = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/BR_Municipios_2022/BR_Municipios_2022.shp"

# 1. Ler CSV de metadados de estações
df_estacoes = pd.read_csv(csv_estacoes)

# 2. Criar pontos geográficos (GeoDataFrame)
gdf_estacoes = gpd.GeoDataFrame(
    df_estacoes,
    geometry=gpd.points_from_xy(df_estacoes['longitude'], df_estacoes['latitude']),
    crs="EPSG:4326"
)

# 3. Ler shapefile dos municípios
gdf_municipios = gpd.read_file(shapefile_municipios)
gdf_municipios = gdf_municipios.to_crs("EPSG:4326")  # garantir mesma projeção

# 4. Spatial join: associar estação ao município
gdf_joined = gpd.sjoin(gdf_estacoes, gdf_municipios, how="left", predicate="within")

# 5. Selecionar colunas úteis
final = gdf_joined[['estacao', 'latitude', 'longitude', 'CD_MUN', 'NM_MUN', 'SIGLA_UF']]

# 6. Exportar resultado
output_csv = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/estacoes_municipios.csv"
final.to_csv(output_csv, index=False)

print(f"✅ CSV salvo com sucesso em:\n{output_csv}")