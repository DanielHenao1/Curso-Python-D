class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad 
    
    # Metodo de la clase Persona    
    def hablar(self):
        print('trabajo para esta empresa')  
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad      
        
    # Metodo de la clase Artista
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"       
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario ):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)  
        self.empresa = empresa
        self.salario = salario
        
    # Metodo de la clase EmpleadoArtista            
    def presentarse(self):
        print(f'Hola soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')
        
        
Empleado1 = EmpleadoArtista('Daniel', 40, 'Colombiano', 'cantar', 'Google', 100000)        

Empleado1.presentarse()


# Como saber si una Clase es una (Subclase) o esta heredado de de otra clase
herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)

# una instancia lo que nos permite ver es que si un objeto es una (instancia) de una clase 
instancia = isinstance(Empleado1,Persona)
print(instancia)


