# < ---------------------------------CREANDO UNA LISTA (list)------------------------------------------- >

# A LAS LISTAS SI LE PODEMOS REASIGNAR VALORES

lista = ['Daniel Henao','DH Store',True,1.79]
# ACONTINUACION REASIGNAMOS EL VALOR AL ELEMENTO 2 SE CAMBIARIA DE TRUE A FALSE
lista [2] = False
print(lista[2])



# < ---------------------------------CREANDO UNA TUPLA (tuple)------------------------------------------- >

# LAS TUPLAS NO SE LE PUEDEN REASIGNAR VALORES
# PARA ACCECDER A LOS VALORES DE LA TUPLA (ACCEDEMOS POR EL INDICE EJEMPLO [0],[1],[2],[3])

tupla = ('Daniel Henao','DH Store',True,1.79)
print(tupla[0])

# ESTO NO SE PUEDE HACER EN LAS TUPLAS

# tupla = ('Daniel Henao','Soy DH', True, 1.79)
# tupla [0] = 'Samuel Henao' 
# print(tupla[0])

# < ---------------------------------CREANDO UN CONJUNTO CON (set)------------------------------------------- >

# LOS CONJUNTOS NO PERMITEN REPETIR VALORES
# TAMPOCO PODEMOS ACCEDER POR EL INDICE 
# PARA ACCEDER A LOS DATOS DE UN CONJUNTO DEBEMOS UTILIZAR UN BUCLE

conjunto = {'Daniel Henao','DH Store',True,1.79,'DH Store'}
print(conjunto)

# ESTO NOS ARROJARIA UN ERROR

# conjunto = {'Daniel Henao','Soy DH', True, 1.79}
# print(conjunto[3])

# < ---------------------------------CREANDO UN DICCIONARIO------------------------------------------- >

diccionario = {
    # clave     # valor
    'nombre' : 'Daniel Henao',
    'web' : 'DH Store',
    'hombre' : True,
    'altura' : 1.79,
    'dato_duplicado' : 'DH Store'
}

# DE LA SIGUIENTE MANERA ACCEDEMOS A LOS DATOS DE UN DICCIONARIO

# PODEMOS ACCEDER A TODOS LOS VALORES 
print(diccionario)

# TAMBIEN PODEMOS ACCEDER ACADA VALOR INDIVIDUAL UTILIZANDO EL NOMBRE QUE TAMBIEN SE CONOCE COMO (clave)
print(diccionario['altura'])