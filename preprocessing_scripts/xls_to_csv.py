import pandas as pd

df = pd.read_excel("POP2024_20241230.xls", engine="xlrd")
df.to_csv("POP2024_20241230.csv", index=False)