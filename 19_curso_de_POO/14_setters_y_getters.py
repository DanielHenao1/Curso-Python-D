# GETTERS

# class Persona:
#     def __init__(self,nombre,edad):    
#         self._nombre = nombre
#         self._edad = edad
    
#     # De esta forma accedemos a un getter    
#     def get_nombre(self):    
#         return self._nombre


# dalto = Persona('Daniel',40)

# nombre = dalto.get_nombre()
# print(nombre)        


# SETTERS y GETTERS 

# Declaramos la clase persona 
class Persona2:
    def __init__(self,nombre,edad):    
        self._nombre = nombre
        self._edad = edad
     
    # Creamos un metodo GETTER    
    def get_nombre(self):
        return self._nombre
    
    # Creamos un metodo SETTER tener en cuenta que este lleva dos parametros 
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
        
# Creamos una instancia o Objeto de la clase persona         
daniel = Persona2('Daniel',40)

# Creamos una variable nombre y asignamos el llamado de la instancia daniel con el metodo get_nombre para obtener el nombre
nombre = daniel.get_nombre()
# Imprimimos la variable nombre que nos tra el valor del objeto en este caso 'Daniel'
print(nombre)

# Utilizamos la instanacia daniel con el metodo set_nombre para reasignar el nombre
daniel.set_nombre('Orlando')

# Despues de reasignar el nombre, llamamos a nuestra instalcia daniel con el metodo get_nombre para obtener el resultado 
nombre = daniel.get_nombre()

# Imprimimos la variable nombre que nos tra el valor del objeto en este caso 'Orlando'
print(nombre)


# De esta forma tambien podemos imprimir el valor de la instancia sin necesidad de crear una variable nueva
print(daniel.get_nombre())

