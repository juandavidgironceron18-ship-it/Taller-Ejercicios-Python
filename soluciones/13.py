import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = df["salario"].astype(str).str.contains(r"[^\d]").sum()

print(f"Hay {cantidad} registros donde el salario tiene caracteres no numéricos.")