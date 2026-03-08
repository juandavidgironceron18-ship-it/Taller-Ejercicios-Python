import pandas as pd

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"],errors="coerce")

cantidad = df[(fecha.dt.year>=1990)&(fecha.dt.year<=2000)].shape[0]

print(f"{cantidad} personas nacieron entre 1990 y 2000.")