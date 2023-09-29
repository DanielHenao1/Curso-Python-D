# EJERCICIO 1.1

# class Estudiante:
#     def __init__(self, nombre, edad, grado): 
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
        
# pedro = Estudiante("Pedro",23,3)        

# print(pedro.nombre)


# EJERCICIO 1.2

class Estudiante:
    def __init__(self, nombre, edad, grado): 
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando....")    
        
    
nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("Por ultimo, su grado: ")


# creamos un objeto llamado estudiante1 con los parametros que se van a pedir al usuario por input()
estudiante1 = Estudiante(nombre,edad,grado)

# Imprimimos los datos que el usuario resgbistro
print(f""" 
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante1.nombre} \n 
      Edad: {estudiante1.edad} \n 
      Grado: {estudiante1.grado} \n 
      """)

# Utilizamos el ciclo while, creamos una variable(estudias.lowwe()) donde por input le preguntamos al usuarios escriba una palabra y no la pase toda a minuscula, y si la palabra escrita es (estudiar) llame a nuestro metodo estudiar() y imprima (estudiando.....)
while True:
    estudias = input()
    if (estudias.lower() == "estudiar"):
        estudiante1.estudiar()