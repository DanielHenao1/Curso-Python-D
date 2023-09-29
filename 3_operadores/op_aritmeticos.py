#suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5 

#multiplicar y dividir (* y /)
multiplicar = 12 * 5
division = 12 / 5 #devuelve un dato float (flotante)

#portenciacion (exponente) (**)
exponente = 12 ** 8

#division baja (//)
division_baja = 12 // 5 #devuelve un entero redondeado hacia abajo 

#resto o modulo 
resto = 12 % 5 #devuelve el rsto de la division


# PARA PODER VERIFICAR EL TIPO DE DATO UTILIZAMOS LA FUNCION (type)

entero = type(5)
flotante = type(5.5)
lista = type(['daniel', 'henao',39,'hombre'])
tupla = type(('daniel', 'henao',39,'hombre'))
conjunto = type({'daniel', 'henao',39,'hombre'})
diccionario = type({
    'nombre' : 'daniel',
    'apellido' : 'henao',
    'edad' : 39,
    'sexo' : 'hombre'})
print(diccionario)
