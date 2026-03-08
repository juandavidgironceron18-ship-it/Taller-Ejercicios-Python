import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = df["email"].astype(str).str.contains(" ").sum()

print(f"Hay {cantidad} registros con espacios adicionales en el email.")