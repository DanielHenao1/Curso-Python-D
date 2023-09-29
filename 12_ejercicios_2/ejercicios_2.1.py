# Fañto el profe y los Guys van a dictar la clase 

# Pedir el nombre y la edad de los compañeros que vinieron hoy a clase 

# Funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    # Creamos la lista con los compañeros
    compañeros = []
    
    # Ejecutamos un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        # La funcion input() siempre nos devuelve un string entonces para que nos de un entero utilizamos la funcion int()
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        # Agregando la informacion a la lista 
        compañeros.append(compañero)
        
    # Ordenandolos de menor a mayor segun su edad con sort() y una funcion lambda    
    compañeros.sort(key=lambda x:x[1])    
    
    # Compañeros [x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # Retornamos una tupla
    return asistente,profesor

# Desempaquetamos lo que nos rfetorna la funcion
asistente,profesor = obtener_compañeros(5)    

# mostrando el resultado
print(f"El asistente es: {asistente} y su profesor es: {profesor}")


