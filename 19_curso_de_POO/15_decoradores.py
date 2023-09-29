# def decorador(funcion):
#     def funcion_modificada():
#         print("Antes de ejecutar la función")   
#         funcion()
#        # print("Despues de llamar a la funcion")
#     return funcion_modificada    
        
   

        
        
# def saludo():
#     print('Hola Daniel como estas')
    
# saludo_modificado = decorador(saludo)    

# saludo_modificado()
    

# Forma optima de utilizar los decoradores de funciones

def decorador(funcion):
    def funcion_modificada():
        print("Antes de ejecutar la función")   
        funcion()
       # print("Despues de llamar a la funcion")
    return funcion_modificada    
        
   

        
        
# def saludo():
#     print('Hola Daniel como estas')
    
# saludo_modificado = decorador(saludo)    

# saludo_modificado()        

@decorador
def saludo2():
    print('Hola daniel como estas')
    
saludo2()    