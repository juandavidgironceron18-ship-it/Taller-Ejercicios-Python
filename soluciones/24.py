import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"]=df["nombre_cifrado"].apply(lambda x:codecs.decode(str(x),'rot_13'))
df["nombre"]=df["nombre"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

df["profesion"]=df["profesion"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = df[(df["nombre"]=="Ana")&(df["profesion"]=="Medico")].shape[0]

print(f"Hay {cantidad} personas llamadas Ana que son Médicos.")