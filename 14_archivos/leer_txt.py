
archivo = open("archivos\\texto_de_dalto.txt")

# leer archivo completo
# archivo = archivo_sin_leer.read()

# leer lineas por lineas
# lineas = archivo_sin_leer.readlines()

# leer una sola linea 
linea = archivo.readline()

archivo.close()

print(linea)