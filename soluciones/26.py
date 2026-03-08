import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"]=df["ciudad"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

activo=df["activo"].astype(str).str.strip().str.lower()

fecha=pd.to_datetime(df["fecha_nacimiento"],errors="coerce")

cantidad = df[(df["ciudad"]=="Barranquilla")&(activo=="true")&(fecha.dt.year>1980)].shape[0]

print(f"Hay {cantidad} personas activas en Barranquilla nacidas después de 1980.")