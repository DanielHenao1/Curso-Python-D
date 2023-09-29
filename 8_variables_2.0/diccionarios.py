
# creando diccionario con dict()

diccionario = dict(nombre='Lucas',apellido='Dalto')

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos

diccionario = {frozenset(['Dalto','rancio']):'DIOS es mi pastor'}

# Creando diccionarios con fromkeys() valor por defecto: none

diccionario = dict.fromkeys(['nombre','apellido','suscriptores'])

print(diccionario)

# Creando diccionarios con fromkeys() cambiando el vaalor por defecto a 'no se'

diccionario = dict.fromkeys(['nombre','apellido'],'no se')

print(diccionario)
