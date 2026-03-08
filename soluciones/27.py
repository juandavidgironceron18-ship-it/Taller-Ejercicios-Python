import pandas as pd

df = pd.read_csv("data/personas.csv")

df["profesion"]=df["profesion"].str.replace(r"[^A-Za-z]","",regex=True).str.title()
df["ciudad"]=df["ciudad"].str.replace(r"[^A-Za-z]","",regex=True).str.title()

ciudad = df[df["profesion"]=="Ingeniero"]["ciudad"].value_counts().idxmax()

print(f"La ciudad con más ingenieros es {ciudad}.")