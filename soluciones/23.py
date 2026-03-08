import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["nombre"]=df["nombre_cifrado"].apply(lambda x:codecs.decode(str(x),'rot_13'))
df["nombre"]=df["nombre"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

df["ciudad"]=df["ciudad"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

cantidad = df[(df["nombre"]=="Carlos")&(df["ciudad"]=="Cali")].shape[0]

print(f"Hay {cantidad} personas llamadas Carlos que viven en Cali.")