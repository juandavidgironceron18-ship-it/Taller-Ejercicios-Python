import pandas as pd

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"],errors="coerce")

cantidad = (fecha.dt.year<1960).sum()

print(f"{cantidad} personas nacieron antes de 1960.")