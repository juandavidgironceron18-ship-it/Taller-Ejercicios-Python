import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"]=df["nombre_cifrado"].apply(lambda x:codecs.decode(str(x),'rot_13'))
df["apellido"]=df["apellido_cifrado"].apply(lambda x:codecs.decode(str(x),'rot_13'))

df["nombre"]=df["nombre"].str.replace(r"[^A-Za-z]","",regex=True).str.title()
df["apellido"]=df["apellido"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = df[(df["nombre"]=="Jose")&(df["apellido"]=="Garcia")].shape[0]

print(f"Hay {cantidad} personas llamadas Jose Garcia en el dataset.")