# creando una funcion que suma numeros
def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pidiendo los numeros
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        # Intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b) 
        # Si lanza una excepcion, pedirle que rfeingrese los numeros    
        except: 
            print('Te pedi un numero amigo, no te hagas el gracioso')  
        # Si todo sale bien terminamos el bucle    
        else:
            break   
        finally:
            print('Esta sentencia poco se utiliza')  
    
    # Mostrando el resultado        
    return resultado
    
    
   

print(sumar_dos())