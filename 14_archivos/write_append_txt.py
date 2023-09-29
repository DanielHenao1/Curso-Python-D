# Creando un archivo desde Python 

# notas = {
#     "Daniel": 100,
#     "Samuel": 99,
#     "Daniela": 98,
#     "Juanpablo": 97
# }

# with open("data_estudiantes.txt", 'w') as archivo:
#     for nombre, nota in notas.items():
#         archivo.write(nombre + " -" + str(nota) + "\n")
        
# Leyendo un archivo desde Python

# with open("data_estudiantes.txt", "r") as file:
#     for linea in file:
#         print("==== char ====")
#         print(linea)        
  
# Agregando datos a un archivo

# nuevasNotas = {
#     "Diana": 96,
#     "Andres": 95,
#     "Candy": 94
# }  

# with open("./data_estudiantes.txt", 'a') as archivo:
#     for nombre, nota in nuevasNotas.items():
#         archivo.write(nombre + " -" + str(nota) + "\n")