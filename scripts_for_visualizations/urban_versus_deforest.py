import pandas as pd
import plotly.express as px

# Caminhos dos arquivos
urban_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/urbanization_growth_rs.csv"
deforestation_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/deforestation_top20_rs.csv"

# Leitura
df_urban = pd.read_csv(urban_path)
df_def = pd.read_csv(deforestation_path)

# Padronização
df_urban['municipality'] = df_urban['municipality'].str.upper()
df_def['municipality'] = df_def['municipality'].str.upper()

# Selecionar os top 20 por área urbanizada em 2013
top20_muns = df_urban.sort_values(by="2013", ascending=False).head(20)['municipality']

# Urbanização (em formato longo)
urban = df_urban[df_urban['municipality'].isin(top20_muns)][['municipality', '2013', '2023']]
urban = urban.melt(id_vars='municipality', var_name='year', value_name='area')
urban['type'] = 'Urban Area'

# Floresta (em formato longo)
forest = df_def[
    (df_def['class_level_2'] == '1.1. Forest Formation') & 
    (df_def['municipality'].isin(top20_muns))
][['municipality', '2013', '2023']]
forest = forest.melt(id_vars='municipality', var_name='year', value_name='area')
forest['type'] = 'Forest'

# Combinar tudo
df_plot = pd.concat([urban, forest], ignore_index=True)

# Garantir ordem correta
df_plot['year'] = df_plot['year'].astype(str)

# Gráfico com animação
fig = px.bar(
    df_plot,
    x="municipality",
    y="area",
    color="type",
    animation_frame="year",
    barmode="group",
    color_discrete_sequence=["#121D40", "#495473"],  # burgundy e azul
    labels={"municipality": "Municipality", "area": "Area (ha)", "type": "Type"}
)

fig.update_layout(
    title="Urban Area vs Forest Cover (2013–2023) – Top 20 RS Municipalities",
    xaxis_tickangle=-45,
    height=600
)

fig.show()

# Salvar o gráfico como HTML
fig.write_html("plots/urban_vs_deforest.html")