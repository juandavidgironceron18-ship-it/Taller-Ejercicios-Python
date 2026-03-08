import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"] = df["ciudad"].astype(str).str.strip()
df["ciudad"] = df["ciudad"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = (df["ciudad"]=="Medellin").sum()

print(f"Hay {cantidad} registros con la ciudad Medellin después de limpiar.")