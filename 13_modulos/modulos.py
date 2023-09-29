# De esta forma importamos un modulo y lo renombramos 

import modulo_saludar as m_saludar

saludo = m_saludar.saludar('Samuel')
print(saludo)

# Tambien podemos imporatar una o varias funciones de un modulo (tambien las podemos renombrar con (as))
from modulo_saludar import saludar,saludar_raro

# Creamos las variables con los saludos
saludo2 = saludar('Daniel')
saludo3 = saludar_raro('Henao')

# Mostramos los resultados
print(saludo2)
print(saludo3)

# Para ver las propiedades y metodos de el namespace
# print(dir(namespace))

# Accedemos al nombre de este modulo 
# print(__name__)

# Accedemos al nombre del modulo llamado 
# print(m_saludar.__name__)