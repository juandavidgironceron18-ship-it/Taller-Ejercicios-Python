import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x),'rot_13'))
df["nombre"] = df["nombre"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = (df["nombre"]=="Juan").sum()

print(f"El nombre Juan aparece {cantidad} veces en el dataset.")