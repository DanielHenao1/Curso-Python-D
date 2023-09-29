# Como cambiar el tipo de dato de una columna 

import pandas as pd 
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")


# Convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)


# Mostrando el tipo de dato del primer elemento de la columna edad
# print(type(df["edad"][0]))


# reemplazando los datos "dalto" por "Maestro"
df["apellido"].replace("dalto","Maestro",inplace=True)


# Eliminando filas con datos faltantes
df = df.dropna()


# Eliminando las filas repedias 
df = df.drop_duplicates()

# Creando un CSV con el datframe resultante(limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")

print(df)


6:53