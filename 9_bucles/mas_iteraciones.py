# Creemos una lista 

frutas = ["banano","manzana","ciruela","pera","naranja","granadilla","durazno"]
cadena = "Daniel Henao"
numeros = [2,15,8,10]

# Cona la sentencia (continue) lo que hacemos es saltarnos la instruccion anteriormente indicada con el (if)
for fruta in frutas:
    if fruta == "granadilla":
        continue
    print(f"Me voy a comer una fruta {fruta}")
    

# Como hacemos para evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una fruta {fruta}")
    if fruta == "pera":
        break
else: 
     print("Bucle terminado")
     
     
# Recorriendo una cadena de texto      

for caracter in cadena:
    print(caracter)
    
    
# For en una sola linea de codigo (duplicamos los numeros)

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)    
    