import pandas as pd

df = pd.read_csv("data/personas.csv")

df["profesion"] = df["profesion"].astype(str).str.strip()
df["profesion"] = df["profesion"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = df["profesion"].nunique()

print(f"Existen {cantidad} profesiones únicas después de normalizar.")