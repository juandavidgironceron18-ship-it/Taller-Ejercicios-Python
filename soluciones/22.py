import pandas as pd
from datetime import datetime

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"],errors="coerce")

edad = (datetime(2026,2,26)-fecha).dt.days/365

cantidad = (edad>50).sum()

print(f"{cantidad} personas tienen más de 50 años.")