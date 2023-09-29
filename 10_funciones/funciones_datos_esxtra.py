# Creando una funcion con 3 parametros

""" def frase(nombre,apelledo,adjetivo):
    return f"Que grande es {nombre} mi {apelledo}, mi {adjetivo}"

frase_resultante = frase("DIOS","pastor","todo")
print(frase_resultante)
 """

# Utyilizando keyword arguments

# frase_resultante = frase(adjetivo ="capo",nombre ="Daniel",apelledo ="Henao")



# Creando la misma funcion con un parametro opcional y un valor por defecto 

def frase(nombre,apellido,adjetivo = "Smart"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Daniel","Henao", adjetivo = "Super Smart")
print(frase_resultante)