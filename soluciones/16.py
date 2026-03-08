import pandas as pd

df = pd.read_csv("data/personas.csv")

salario = pd.to_numeric(
df["salario"].astype(str).str.replace(r"[^0-9]","",regex=True),
errors="coerce"
)

print(f"El salario mínimo después de limpiar es {salario.min()}.")