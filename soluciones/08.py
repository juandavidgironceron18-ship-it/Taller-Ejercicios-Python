import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"] = df["ciudad"].astype(str).str.strip()
df["ciudad"] = df["ciudad"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = df["ciudad"].nunique()

print(f"Existen {cantidad} ciudades únicas después de normalizar.")