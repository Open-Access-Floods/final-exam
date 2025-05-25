import pandas as pd
import plotly.express as px

# Caminho para o arquivo
file_path = "/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/urbanization_growth_rs.csv"

# Carregar os dados
df = pd.read_csv(file_path)

# Ordenar pelos maiores valores de 2013
df_top_20 = df.sort_values(by="2013", ascending=False).head(20)

# Gráfico de barras comparando 2013 e 2023
fig = px.bar(
    df_top_20,
    x="municipality",
    y=["2013", "2023"],
    barmode="group",
    title="Top 20 Urbanized Municipalities in RS (by 2013 Area)",
    labels={"value": "Urban Area (ha)", "variable": "Year"},
    color_discrete_sequence=["#7f2a3c", "#c8646e"]  # Burgundy tones
)

fig.update_layout(
    xaxis_title="Municipality",
    yaxis_title="Urban Area (ha)",
    legend_title="Year",
    xaxis_tickangle=45
)

fig.show()