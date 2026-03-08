import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = df["id"].astype(str).str.contains(r"\D").sum()

print(f"Hay {cantidad} filas donde el campo id tiene caracteres no numéricos.")