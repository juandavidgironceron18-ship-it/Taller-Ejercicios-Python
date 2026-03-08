import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x),'rot_13'))
df["nombre"] = df["nombre"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

nombre = df["nombre"].value_counts().idxmax()
cantidad = df["nombre"].value_counts().max()

print(f"El nombre más frecuente es {nombre} y aparece {cantidad} veces.")