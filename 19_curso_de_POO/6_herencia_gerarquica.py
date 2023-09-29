# Herencia Gerarquica es cuando varias clases dependen de una misma clase

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad 
        
    def hablar(self):
        print('Hola trabajo para esta empresa')  
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)        
        self.trabajo = trabajo
        self.salario = salario
        
class Profesor(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, materias):
        super().__init__(nombre, edad, nacionalidad)        
        self.notas = notas
        self.materias = materias
        
class Rector(Persona):
    def __init__(self, nombre, edad, nacionalidad, aprobados, masters):
        super().__init__(nombre, edad, nacionalidad)
        self.aprobados = aprobados
        self.masters = masters        
        
Usuario1 = Profesor("Pedro",39,"colombiano",100,"programacion")

print(Usuario1.materias)