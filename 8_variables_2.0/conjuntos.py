# Creando un conjunto con set()
conjunto = set(['Dato 1'])

# Metiendo un conjunto dentro de otro conjunto con frozenset()
conjunto1 = frozenset(['Dato 1','Dato 2'])
conjunto2 = {conjunto1,'Dato 3'}
print(conjunto2)

# Teoria de los conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {9,2,0}

# Verificando si es un subconjunto 

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1


# Verificando si es un superconjunto

resultado2 = conjunto2.issuperset(conjunto1)
resultado2 = conjunto2 > conjunto1

# Verificando si hay algun numero en comun

resultado3 = conjunto2.isdisjoint(conjunto1)

print(resultado3)