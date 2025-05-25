import geopandas as gpd

shapefile_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/RG2017_rgint_20180911"

gdf = gpd.read_file(shapefile_path)
print(gdf.columns)
