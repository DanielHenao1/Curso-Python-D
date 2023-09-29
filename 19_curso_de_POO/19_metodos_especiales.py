class Persona:
    def __init__(self,nombre, edad):    
        self.nombre = nombre
        self.edad = edad
    
    # def __str__(self):
    #     return  f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    
daniel = Persona('Henao',40)
samuel = Persona('Quevedo',9)
maria = Persona('Caldas',81)

nueva_persona = daniel + samuel + maria

print(nueva_persona.edad)