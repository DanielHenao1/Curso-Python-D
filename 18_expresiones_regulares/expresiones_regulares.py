import re

texto = """Hola maestro,. esta el la cadena 1. como estas mi capitan
esta es la linea. 252 de texto,
y esta es la final. (linea 3) definitiva mi capitan"""

# Haciendo una busqyeda simple            
#resultado = re.findall("a", texto)

# \d -> busca digitos numericos del 0 al 9
#resultado = re.findall(r'\d',texto)

# \D -> Busca todo menos digitos numericos
#resultado = re.findall(r'\D',texto)

# \w -> Busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r'\w',texto)

# \s -> Busca espacios en blanco y saltos en linea
# resultado = re.findall(r'\s',texto)

# \S -> Busca todo menos espacion en blanco y saltos de linea
#resultado = re.findall(r'\S',texto)

# . -> Busca todo menos saltos de linea
#resultado = re.findall(r'.',texto)

# \n -> Busca saltos en linea
#resultado = re.findall(r'\n',texto)

# \ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r'\.',texto)


# Armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r'\d\.\s',texto)

# Buscado el principio de una linea
#^ -> busca el comienzo de una linea
#resultado = re.findall(r'^Hola',texto)

# Buscado el principio de cada linea
#^ -> busca el comienzo de cada linea de un texto
#resultado = re.findall(f'^esta',texto, flags=re.M)

# Buscando el final de una linea
#$ -> busca el fin de una linea
#resultado = re.findall(r'capitan$',texto,flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r'\d{3}\s',texto)

# {n,m} -> al menos n, como maximo m
#resultado = re.findall(r'\d{1,4}',texto)

# | -> busca una cosa o la otra 
resultado = re.findall(r'\d{1,4}|Hola',texto)

print(resultado)            
            