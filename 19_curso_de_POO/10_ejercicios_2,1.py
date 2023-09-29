# Ejercicio 2.1 

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
        
#     def mostrar_datos(self):
#         pass
#        # print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")    
        
# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
        
#     def mostrar_grado(self):
#         print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años y estoy cursando el grado de {self.grado} en ingenieria de sistemas")    
    
    
# estudiante1 = Estudiante('Daniel',40,'Profesional')

# estudiante1.mostrar_grado()      


 

# Otra forma de dar solucion al ejercicio 2.1

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'edad: {self.edad}')
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)    
        self.grado = grado 

    def mostrar_grado(self):
        print(f'Grado: {self.grado}')       
        

estudiante1 = Estudiante('Daniel',40,'Profesional')

estudiante1.mostrar_datos()
estudiante1.mostrar_grado()
                