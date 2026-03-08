import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["apellido"] = df["apellido_cifrado"].apply(lambda x: codecs.decode(str(x),'rot_13'))
df["apellido"] = df["apellido"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

apellido = df["apellido"].value_counts().idxmax()
cantidad = df["apellido"].value_counts().max()

print(f"El apellido más frecuente es {apellido} y aparece {cantidad} veces.")