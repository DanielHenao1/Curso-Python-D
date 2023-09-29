# Creando una funcion lambda para multiplicar por 2

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))


# Creemos una lista 
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20]

# Creando una funcion comun que diga si es par o no 
def es_par(num):
    if (num%2==0):
        return True

# Usando filter con una funcion comun 
numeros_pares = filter(es_par,(numeros))

print(list(numeros_pares))


# creando lo mismo pero con la funcion lambda()

numeros_pares = filter(lambda num:num%2 == 0,numeros)
print(list(numeros_pares))