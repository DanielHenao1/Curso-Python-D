# Creando una funcion que nos devuelva los numeros primos 
# Entre cero y el argumento que pasamos 


# Crear una funcion que verifique si un numero es primo
def es_primo(num):
    # Verificamos que el numero pasado no pueda dividirse 
    # por ningun numero entre 2 y ese mismo numero menos 1
    for i in range(2,num-1):
        # Si es divisible por alguno retornamos falso y termina el bucle 
        if num%i==0: return False
    # Si termina el bucle, significa que no fue divisible entonces es primo    
    return True


# Crear una funcion que verifique si un numero es primo
def primos_hasta(num):
    # Creamos la lista 
    primos = []
    for i in range(3,num-1):
        # Verificamos si el numero es primo
        resultado = es_primo(i)
        # en caso de que sea lo agregamos a la lista 
        if  resultado == True: primos.append(i)
    # Devolvemos la lista     
    return primos    

# Creamos el resultado llamando a la lista y lo mostramos 
resultado = primos_hasta(13)
print(resultado)    
            