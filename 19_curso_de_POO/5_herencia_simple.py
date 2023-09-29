# Herencia Simple

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad 
        
    def hablar(self):
        print('Hola, Estoy hablando un poco')    
        
# Aca podemos ver que la clase Empleado hereda los parametros de la clase Persona
class Empleado(Persona):
   # pass # esto lo utilizamos cuando creamos una clase pero no le agregamos info y no la vamos a utilizar en el momento pero la dejamos creada
   
   
 def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

diana = Empleado("Diana",39,"argentino","Programador",100000)
        
diana.hablar()  