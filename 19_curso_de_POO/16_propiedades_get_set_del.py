
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    # @property es un decorador reservado para las clases(cuando utilizo este para el llamado no hay que utilizar ())
    # este lo utilizamos para obtener datos es como utilizar un getter() pero la forma optima
    @property  # esto es igual a getter 
    def nombre(self):
        return self.__nombre
    
    # esto es como se utiliza un setter de forma optima(lo utilizamos para modificar una propiedad de forma optima)
    @nombre.setter # esto es igual a un setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
        
    @nombre.deleter  # esto lo utilizamos para eliminar valores
    def nombre(self):
        del self.__nombre
    
    
dalto = Persona('Daniel',40)

nombre = dalto.nombre
print(nombre)    
        
dalto.nombre = 'pepe' 
            
nombre = dalto.nombre
print(nombre)    
        

dalto.nombre = 'pepe' 
            
nombre = dalto.nombre
print(nombre)    