# Creamos la clase sin parentesis
class Celular:
    # Metodo especial para crear atributos de instancias
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
        
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

# Imprimimos 
print(celular2.modelo)