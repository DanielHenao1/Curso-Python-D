
""" # Sepuede crear una lista con la funcion (list) OJO ESTO YA NO SE USA
lista = list(['hola','dani','34']) """

lista = ['Daniel Henao','DH Store',True,1.79]
lista2 = [9,53,7,6,21,0,15,38]

""" # Metodo (len) cuenta los elementos de una lista (OJO) LEN NO ES UN METODO ES UNA (FUNCION)

cantidad_elemntos = len(lista)

print(cantidad_elemntos) """

""" # Metodo (append) Agrega un elemento a la lista

lista.append('Samuel Henao')

print(lista) """

""" # Metodo (insert) Agrega un elemento a la lista en un indice especifico

lista.insert(2, 'Samuel Henao')

print(lista) """

""" # Metodo (insert) Agrega Varios elemntos a una lista (lo que se va agregar se debe pasar como una lista [])

lista.extend([False, 2023, 'Samuel henao'])

print(lista) """

""" # Metodo (pop) elimina un elemento de una lista, pide el indice (para eliminar el ultimo elemento de una lista ponemos -1)

print(len(lista))

lista.pop(2)

print(len(lista)) """

""" # Metodo (remove) Removiendo un elemento de la lista por su valor

lista.remove(True)

print(lista) """

""" # Metodo (clear) Elimina todos los elemntos de una lista

lista.clear()

print(lista) """

""" # Metodo (sort) Organiza los numeros en orden acsendente y si ponemos 

lista2.sort()
# con el metodo (reverse) lo que hacemos en invertir el orden de los numeros
lista2.sort(reverse=53)

print(lista2) """

""" # Metodo (revere) Invierte los elemntos de una lista

lista2.reverse()

print(lista2) """

""" # Con lo siguiente podemos ver que metodos o funciones podemos aplicar a cada tipo de dato
    # (LISTAS), (TUPLAS), (CONJUNTOS), (DICCIONARIOS).

print(dir(list))
print(dir(tuple))
print(dir(set))
print(dir(dict)) """

