numeros = [4,7,79,15]

# Encontrando el numero mayor de una lista con funcion max()

numero_mas_alto = max(numeros)
print(numero_mas_alto)


# Encontrando el numero menor de una lista con funcion min()

numero_menor = min(numeros)
print(numero_menor)


# Redondeando a 6 decimales con la funcion round()
# Podemos ver un ejemplo de optimizacion de codigo en los ejercicios 1.1

numero = round(12.345678,2)
print(numero)


# la funcion bool() si le pasamos un valor -> vacio, False, None \ True -> nos devuelve (False)

resultado_bool = bool(0)
print(resultado_bool)


# La funcion all() nos devuelve (True) si todos los valores son verdaderos 

resultado_all = all([5,"true",[344,23]])
print(resultado_all)


# La funcion sum() suma todos los valores de un iterable

suma_total = sum(numeros)
print(suma_total)


