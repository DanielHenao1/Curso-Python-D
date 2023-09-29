# Ejemplo de un atributo privado

# class MiClase:
#     def __init__(self):
#         # Con un _despues de self queremos indicar que es un atributo privado, pero los desarroladores lo pueden ver
#         self._atributos_privados = 'valor'
  
# # Creamos un objeto de la clase prinsipal MiClase        
# objeto = MiClase()

# # Imprimimos objeto y funcion
# print(objeto._atributos_privados)        


# Ejemplo de un atributo muy muy privado

class MiClase:
    def __init__(self):
        # Con dos __despues de self queremos indicar que es un atributo privado, pero los desarroladores lo pueden ver
        self.__atributos_privados = 'valor'
        
    # Tambien existen los metodos Privados
    def _hablar(self):
        return 'Hola como estas'
    
    # Tambien existen los metodos muy muy pribados
    def __hablar(self):
        return 'Hola buenos dias' 
  
# Creamos un objeto de la clase prinsipal MiClase        
objeto = MiClase()

# Imprimimos objeto y funcion
print(objeto._hablar()) 