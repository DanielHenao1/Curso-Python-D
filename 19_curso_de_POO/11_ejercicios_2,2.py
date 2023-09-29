# Ejercicio 2.2

# Creamos clase principal Animal
class Animal:
    # Creamos Metodo comer
    def comer(self):
        print('El animal esta comiendo')
        
# creamos subclase Ave que tiene herencia de la clase principal Animal
class Ave(Animal):
    # Creamos metodo volar
    def volar(self):
        print('El animal esta volando')

# creamos subclase Mamifero que tiene herencia de la clase principal Animal
class Mamifero(Animal):
    # Creamos metodo amamantar
    def amamantar(self):
        print('El animal esta amamantando')
        
# creamos subclase Murcielago que tiene herencia de las subclases Mamifero y Ave        
class Murcielago(Mamifero, Ave):
    pass

# creamos un objeto o animal instanciado en la clase Murcielago
murcielago1 = Murcielago()

# Imprimimos todos los metodos y funciona correctamete 
murcielago1.comer()
murcielago1.volar()
murcielago1.amamantar()

# # Creamos el objeto o animal ave
# ave = Ave()

# # Imprimimos todos los metodos, pero nos arrojaria error por que ave no tiene heredado el metodo amamantar
# ave.comer()
# ave.volar()
# # ave.amamantar()



# Averiguamos si Ave es una subclase de Animal
herencia = issubclass(Ave, Animal)
print(herencia)

# Tambien podemos ver el mro (Metodo de Resolucion de Orden)
print(Murcielago.mro())