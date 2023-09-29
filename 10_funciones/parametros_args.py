# Forma no optima de sumar valores

""" 
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados    

resultado = suma([5,3,9])
 """


# Forma optima utilizando el parametro args(*)

def suma(*numeros):
    return sum(numeros)

resultado = suma(4,5,6,7,9)
print(resultado)

# Tambien podemos utilizar el parametro args(*) con mas argumentos 

def suma2(nombre,*numbers):
    return f"Hola {nombre} el total de tus numeros sumados es: {sum(numbers)}"

resultado2 = suma2("Daniel",4,5,6,7,9)
print(resultado2)

# ESTA LA FORMA MAS OPTIMA DE SUMAR VALORES USANDO EL PARAMETRO ARGS (*)

def suma3(numbers2):
    return sum([*numbers2])

resultado3 = suma3([4,5,6,7,9])
print(resultado3)
