import pandas as pd
import geopandas as gpd

# Caminhos atualizados
csv_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_pre_processed/chuva_por_municipio.csv"
shp_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/BR_Municipios_2022/BR_Municipios_2022.shp"
output_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/chuva_rs.geojson"

# Carrega dados de precipitação
df_chuva = pd.read_csv(csv_path)
df_chuva["Município"] = df_chuva["Município"].str.strip().str.upper()

# Carrega shapefile e filtra apenas RS
gdf_mun = gpd.read_file(shp_path)
gdf_mun = gdf_mun[gdf_mun["SIGLA_UF"] == "RS"]
gdf_mun["NM_MUN"] = gdf_mun["NM_MUN"].str.strip().str.upper()

# Faz o merge com base no nome do município
gdf_rs = gdf_mun.merge(df_chuva, left_on="NM_MUN", right_on="Município", how="inner")

# Salva como GeoJSON para visualizações
gdf_rs.to_file(output_path, driver="GeoJSON")
print("✅ GeoJSON criado com sucesso:", output_path)