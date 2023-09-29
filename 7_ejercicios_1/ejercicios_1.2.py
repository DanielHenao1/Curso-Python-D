# Le pedimos a un usuario que nos diga una frase (o varias)

frase = input('Decime una frase y te calculo cuanto tiempo tardarias si tuvieras que decirla: ')

# Creamos una lista con todas las palabras de la lista (se separan cada vez que haya un espacio en blanco)

palabras_separadas = frase.split(' ')

# Usamos len() para ver que cantidad de elemntos hay en la lista

cantidad_de_palabras = len(palabras_separadas)

# En caso de que tarde mas de un minuto decirlo, le decimos que pare un poco.

if cantidad_de_palabras > 120:
    print('Para tio tampoco te pedi un testamento')
    
# Calculemos cuanto tardaria en decir las palabras y se lo decimos 

print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dani lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')
    