diccionario = {
    'nombre' : 'Daniel',
    'apellido' : 'Henao',
    'suscrib' : 100000
}


""" # Metodo (keys) Devuelve las claves (tambien nos sirve para iterar o recorer datos)

claves = diccionario.keys()

print(claves) """

""" # Metodo (get) Devuelve el valor de una clave (si no encuentra nada el programa continua (no lanza ninguna excepcion))

claves = diccionario.get('nombre')

print(claves) """

""" # Metodo (clear) Elimina todos los elementos del diccionario

diccionario.clear()

print(diccionario) """

""" # Metodo (pop) Elimina un elemento del diccionario

diccionario.pop('nombre')

print(diccionario) """

# Metodo (items) Para iterar el diccionario (ejemplo de como se obtiene un elemento dict_items iterable)

diccionario_iterable = diccionario.items()

print(diccionario_iterable)

