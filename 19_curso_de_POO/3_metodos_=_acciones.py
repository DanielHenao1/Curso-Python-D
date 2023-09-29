# Un metodo lo podemos definir que es una funcion 
# Todas la funciones que creemos dentro de una clase se llaman metodos

# SIEMPRE ES INDISPENSABLE definir cuando creamos una clase def __init__(self)

# Creamos la clase sin parentesis
class Celular:
    
    # Metodo especial para crear atributos de instancias
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    # Esta funcion la denominamos como un (metodo)
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")    
     
    # Esta funcion la denominamos como un (metodo)    
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")    

# Creamos 2 objetos diferentes        
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

# Imprimimos 
celular2.llamar()



