import pandas as pd

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"],errors="coerce")

cantidad = fecha.isna().sum()

print(f"Hay {cantidad} registros con fecha de nacimiento en formato incorrecto.")