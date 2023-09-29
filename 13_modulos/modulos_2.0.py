# Si el modulo estuviera dentro de una carpeta en la misma ruta se importa asi:

""" import funciones_buenas.saludar as m_saludar

print(m_saludar.saludar('Daniel'))
 """
 
 # De esta manera agregamos una ruta con la funcion sys() sys es un modulo construido en python
 

import sys 
 
# Esto nos devuelve una tupla con todos los valores de las propiedades similar a (dir) 
# print(sys.builtin_module_names) 
 

# Con esto podemos ver una lista con las rutas de los modulos  
# print(sys.path) 


# Con esto agragamos una ruta de una carpeta para poder accede desde este archivo y ejecutarlo
sys.path.append("C:\\Users\\DhTec\\OneDrive\\Escritorio\\Curso de Python\\funciones_buenas")
# print(sys.path)

""" import saludar 

print(saludar.saludar('Daniel')) """

