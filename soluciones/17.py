import pandas as pd

df = pd.read_csv("data/personas.csv")

activo = df["activo"].astype(str).str.strip().str.lower()

cantidad = (activo=="true").sum()

print(f"Hay {cantidad} registros con activo = verdadero.")