import geopandas as gpd

# Caminho para o shapefile das regiões intermediárias
shp_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/RG2017_rgint_20180911"

# Carrega o shapefile
gdf = gpd.read_file(shp_path)

# Filtra apenas as regiões do RS (códigos que começam com 43)
gdf_rs = gdf[gdf["rgint"].astype(str).str.startswith("43")]

# Salva como GeoJSON
output_geojson = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/regioes_intermediarias_rs.geojson"
gdf_rs.to_file(output_geojson, driver="GeoJSON")

print("✅ GeoJSON das regiões intermediárias do RS salvo com sucesso!")