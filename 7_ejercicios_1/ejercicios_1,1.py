
# Promedios de duraciones

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dani_curso = 1.5

# Duracion de crudo

crudo_promedio = 5
crudo_dani = 3.5

# Diferencias de duracion

""" diferencia_con_min = 100 - dani_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dani_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dani_curso / otros_cursos_promedio * 100

# Calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dani = 100 - dani_curso * 1000 // crudo_dani /10

# Mostrando las diferencias de duracion del curso (ejercicio A)

print('---------------------------------')
print(f'El curso de daniel dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de daniel dura un {diferencia_con_max}% menos que el mas rapido')
print(f'El curso de daniel dura un {diferencia_con_promedio}% menos que el mas rapido')
print('---------------------------------')

# Mostrando la cantidad de espacios vacios que se remueven (CRUDO) - (ejercicio B)

print(f'Un curso promedio elimina un tiempo de {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dani}% de tiempo vacio')
print('---------------------------------')

# Mostrando diferencias si los cursos duran 10 horas 

print(f'Ver 10 horas de este curso equivalen a ver {otros_cursos_promedio * 100 // dani_curso / 10}')
print(f'Ver 10 horas de otros curso equivalen a ver {dani_curso * 100 // otros_cursos_promedio / 10}')
print('---------------------------------') """


# La forma como se debe redondear decimales es con la funcion round() en los anteriores ejemplo se puede hacer pero no es lo mas optimo

# Diferencias de duracion
diferencia = dani_curso / otros_cursos_max
print(round(diferencia,4))
