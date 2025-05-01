import pandas as pd
import geopandas as gpd
from shapely.geometry import shape
import json

# Caminhos
csv_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/UrbanRisk_MapBiomas_2022.csv"
shapefile_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/BR_Municipios_2022/BR_Municipios_2022.shp"

# 1. Carrega os dados de risco
df = pd.read_csv(csv_path)
df["geometry"] = df[".geo"].apply(lambda g: shape(json.loads(g)))
gdf_risco = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# 2. Carrega os municípios
gdf_municipios = gpd.read_file(shapefile_path)

# 3. Reprojetar para sistema métrico (área em m²)
gdf_risco = gdf_risco.to_crs("EPSG:5880")
gdf_municipios = gdf_municipios.to_crs("EPSG:5880")

# 4. Interseção espacial
intersec = gpd.overlay(gdf_risco, gdf_municipios, how="intersection", keep_geom_type=False)

# 5. Calcular área em risco por município
intersec["area_risco_km2"] = intersec.geometry.area / 10**6

# 6. Agrupar por município
result = intersec.groupby("CD_MUN_2").agg({
    "area_risco_km2": "sum",
    "NM_MUN_2": "first",
    "SIGLA_UF": "first"
}).reset_index()

# 7. Calcular área total do município
gdf_municipios["area_municipio_km2"] = gdf_municipios.geometry.area / 10**6
area_total = gdf_municipios[["CD_MUN", "area_municipio_km2"]]

# 8. Juntar
final = result.merge(area_total, left_on="CD_MUN_2", right_on="CD_MUN", how="left")
final["perc_area_em_risco"] = (final["area_risco_km2"] / final["area_municipio_km2"]) * 100

# 9. Exportar CSV
output_csv = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/mapbiomas_area_em_risco_por_municipio.csv"
final.to_csv(output_csv, index=False)

print(f"✅ CSV final salvo com sucesso em:\n{output_csv}")
