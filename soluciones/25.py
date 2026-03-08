import pandas as pd

df = pd.read_csv("data/personas.csv")

df["profesion"]=df["profesion"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

salario=pd.to_numeric(df["salario"].astype(str).str.replace(r"[^0-9]","",regex=True),errors="coerce")

cantidad = df[(df["profesion"]=="Abogado")&(salario>10000000)].shape[0]

print(f"Hay {cantidad} abogados con salario mayor a 10,000,000.")