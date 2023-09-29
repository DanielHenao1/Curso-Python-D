# MRO metodo de resolucion de orden

# Ejercicio 2 de MRO (Ramificacion)

class A:
    pass
    # def hablar(self):
    #     print('Hola desde A')

class F:
    def hablar(self):
        print('Hola desde F')

class B(A):
    pass
    # def hablar(self):
    #     print('Hola desde B')
    
class C(F):
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
# En el segundo llamado se ejecuta desde B
# En el tercer llamado se ejecuta desde A por que es la primera clase padre que comienza heredando
# En el cuarto llamado se ejecuta desde C por que esta hereda de la clase padre F
# En el quinto llamado se ejecuta desde F por que es la segunda clase padre que sigue heredando


# Con lo siguiente podemos ver el orden de ejecucion de una clase
print(D.mro())
