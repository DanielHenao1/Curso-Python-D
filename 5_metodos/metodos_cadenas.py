# UN METODO ES UNA FUNCION APLICADA A OBJETOS 

cadena1 = 'Daniela es mi hija'
cadena2 = 'DIOS es mi pastor'

""" # (dir) no es un METODO es una (FUNCION) ejemplo de ejecucion

print(dir(cadena1))
 """

# < --------------------------------- METODOS PARA TRABAJAR CON CADENAS------------------------------------------- >

""" # Metodo (upper) para convertir a mayusculas

mayusc = cadena1.upper()

print(mayusc)
 """


""" # Metodo (lower) para convertir a minusculas

minusc = mayusc.lower()

print(minusc) """


""" # Metodo (capitalize) para convertir la primera letra en mayuscula

first_in_mayus = minusc.capitalize()

print(first_in_mayus)
 """


""" # Metodo (find) para buscar una cadena en otra cadena, si no hay concidencias nos devuelve -1

busqueda_find = cadena1.find('a')

print(busqueda_find) """


""" # Metodo (index) para buscar una cadena en otra cadena, si no hay concidencias nos devuelve una exepcion

busqueda_index = cadena1.index('5')

print(busqueda_index) """


""" # Metodo (isnumeric) para buscar una cadena si es numerico devuelve TRUE

es_numerico = cadena1.isnumeric()

print(es_numerico) """


""" # Metodo (isalpha) para buscar una cadena si es alfa numerico devuelve TRUE

es_alfanumerico = cadena1.isalpha()

print(es_alfanumerico) """


""" # Metodo (count) devuelve el numero de coincidencias de una subcadena en la cadena dada

contar_coincidencias = cadena1.count('a')

print(contar_coincidencias) """


""" # Metodo (len) cuenta los caracteres de una cadena (OJO) LEN NO ES UN METODO ES UNA (FUNCION)

contar_caracteres = len(cadena1)

print(contar_caracteres) """


""" # Metodo (endswith) Verifica si una cadena termina con otra cadena dada, si es asi devuelve TRUE

termina_con = cadena1.endswith('hija')

print(termina_con) """


""" # Metodo (startswith) Verifica si una cadena comienza con otra cadena dada, si es asi devuelve TRUE

comienza_con = cadena1.startswith('Daniela')

print(comienza_con) """


""" # Metodo (replace) Reemplaza una parte de la cadena dada por la que le demos, debe existir el valor que queremos reemplazar

cadena_nueva = cadena1.replace('Daniela','Danielu')

print(cadena_nueva) """


""" # Metodo (split) crea una lista con la cadena que le pasemos (separa la cadena y la convierte en una lista)

cadena_separada = cadena1.split()

print(type(cadena_separada)) """
