""" 
# Creando una funcion simple con (def) creamos nuestras propias funciones

def saludar():
    print("DIOS es mi pastor nada me faltara")

# Ejecutando una funcion simple    
saludar()
"""

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
            
    print(f"Hola {nombre}, mi {adjetivo} como estas?")

# Ejecutando la funcion saludar() esta funcion la creamos nosotros mismo
saludar("Daniel","Hombre")    
saludar("Diana","Mujer")    
saludar("Daniel","Ejemplo")    


# Creando una funcion que nos retorne valores

def crear_contraseña_random(num):
    chars = "abdcefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
password = crear_contraseña_random(5)    
frase = f"Tu contraseña nueva es: {password}"
print(frase)


# Desempaquetando y devolviendo dos valores 

def crear_contraseña_random(num):
    chars = "abdcefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
password,primer_numero = crear_contraseña_random(5)    
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")




