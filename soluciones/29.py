import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = df["email"].astype(str).str.contains("@gmail.com").sum()

print(f"Hay {cantidad} registros con email del dominio gmail.com.")