class Gato():
    def sonido(self):
        return "Miau"
    
    
class Perro():
    def sonido(self):
        return "Guau"
    
    
# Creemos una funcion independiente de las clases 

def hacer_sonido(animal):
    print(animal.sonido())

# Aplicando POLIFORMISMO

# Creamos objeto Gato
gato1 = Gato()

# Creamos objeto Perro
perro1 = Perro()


# print(perro1.sonido())
# print(gato1.sonido())

hacer_sonido(gato1)
hacer_sonido(perro1)

# Duck Typing
# Enlaces dinamicos 
# Enlaces estaticos
# Tipo real
# Tipo declarado