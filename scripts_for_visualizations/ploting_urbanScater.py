import pandas as pd
import plotly.express as px

# Carrega os dados
df = pd.read_csv("/Users/carlamenegat/Documents/GitHub/Untitled/final-exam/data_for_visualizations/urbanization_growth_rs.csv")

# Cria a coluna de crescimento
df["growth"] = df["2023"] - df["2013"]

# Cria o scatter plot
fig = px.scatter(
    df,
    x="2013",
    y="2023",
    color=df["growth"].apply(lambda x: "Growth" if x > 0 else "Decline" if x < 0 else "No Change"),
    hover_name="municipality",
    labels={"2013": "Urban Area (2013)", "2023": "Urban Area (2023)", "color": "Change"},
    title="Urban Area Growth – Municipalities of RS (2013 vs 2023)",
    trendline_scope="overall"
)

# Adiciona linha de referência 45° (x = y)
fig.add_shape(
    type="line",
    x0=df["2013"].min(), y0=df["2013"].min(),
    x1=df["2013"].max(), y1=df["2013"].max(),
    line=dict(color="gray", dash="dash"),
    name="No Change Line"
)

fig.update_layout(legend_title_text="Growth Status")

fig.show()