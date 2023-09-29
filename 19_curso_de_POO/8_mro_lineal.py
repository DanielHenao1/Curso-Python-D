# MRO metodo de resolucion de orden 

# Ejercicio 1 de MRO (Lineal)

class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    pass
    # def hablar(self):
    #     print('Hola desde B')

class C(A):
    pass
    # def hablar(self):
    #     print('Hola desde C')

class D(B,C):
    pass
    # def hablar(self):
    #     print('Hola desde D')
        
        
# Creando un objeto llamado d
d = D()

d.hablar()        


# En al primer llamado se ejecuta desde D
# En el segundo llamado se ejecuta desde (B) por que es el primer parametro que le pasamos a (D)
# En el tercer llamado se ejecuta desde (C) por que es el segundo parametro que le pasamos a (D)
# En el cuarto llamado se ejecuta desde (A) por que es la clase padre


# Consultando subclases
# herencia = issubclass(A, B)
# print(herencia)

print(D.mro())
# Con lo siguiente podemos ver el orden de ejecucion de una clase

#  <------------------------------------- Ejercicio 2 -------------------------------------->

# Ejercicio 2 de MRO llamando cualquier clase

class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')

class C(A):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    def hablar(self):
        print('Hola desde D')
        
        
# Creando un objeto llamado d
d = D()

# Tambien podemos ejecutar la clase y su metodos de la siguiente manera 
C.hablar(d)