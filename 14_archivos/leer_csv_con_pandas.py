# py -m pip install --upgrade pip (comando para actualizar pip desde cdm)

import pandas as pd 

df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# Obteniendo los datos de la columna nombre
# print(df["nombre"])


""" # Con print(variable[:]) podemos extraer partes de codigo o de una cadena especifica ejemplo
cadena = "danielHenao"

print(cadena[2:8]) # este arrojaria (nielHe) """

# Ordenando el dataframe por la edad 
df_orden_ascendente = df.sort_values("edad")

# Ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)


# Concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

# Accediendo a las primeras filas con head()
primeras_filas = df.head(4)


# Accediendo a las ultimas filas con teil()
ultimas_filas = df.tail(2)


# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape


# Obteniendo data estadistica del dataframe
df_info = df.describe()


# Accediendo a un documento especifico del datframe con (loc)
elemento_especifico_loc = df.loc[2,"edad"]


# Accediendo a un documento especifico del datframe con (iloc)
elemento_especifico_iloc = df.iloc[2,2]


# Accediendo a todas las filas de una columna con (iloc)
edades = df.iloc[:,0]

# Accediendo a todas las columnas de una fila con (loc)
fila_3 = df.loc[2,:]

# Accediendo a todas las columnas de una fila con (iloc)
fila_3 = df.iloc[2,:]

# Acceder a filas utilizando una condicion
# El primer dato son las filas : Segundo dato las columnas
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)