import pandas as pd

df = pd.read_csv("data/personas.csv")

# limpiar profesión
df["profesion"] = df["profesion"].astype(str).str.strip()
df["profesion"] = df["profesion"].str.replace(r"[^A-Za-z]", "", regex=True).str.title()

# limpiar salario y convertirlo a número
df["salario_limpio"] = pd.to_numeric(
    df["salario"].astype(str).str.replace(r"[^0-9]", "", regex=True),
    errors="coerce"
)

# calcular salario promedio por profesión
profesion = df.groupby("profesion")["salario_limpio"].mean().idxmax()

print(f"La profesión con el salario promedio más alto es {profesion}.")