animales = {"pez","perro","gato","loro","cocodrilo"}
numeros = {10,20,30,40,50}

# Recorriendo la conjunto animales

for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    

# Recorriendo la conjunto numeros y multiplicando cada valor por 10

for numero in numeros:
    resultado = numero * 10
    print(resultado)
    

# Recorriendo dos conjuntos en el mismo bucle for, (tener en cuenta que las dos conjuntos debe tener las mismas cantidad de elementos)
# puede iterar las conjuntos que quiera en el mismo bucle (for) 
    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo conjunto 1: {numeros}")    
    print(f"recorriendo conjunto 2: {animales}")    
    

# Otra forma correcta de recorrer una conjunto con su indice y con enumerate()

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

# Forma correcta de recorrer una conjunto por su indice (recorremos el indice y el valor en un mismo (for) usando la funcion enumerate())

for number, indice in enumerate(numeros):
    print(f"el indice es: {number} y el valor es: {indice}")
   

# Usando (for/else) en un bucle

for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")         