# si la accion es verdadera el codigo se ejecuta, pero si es falsa se ejecuta el else

edad = 17

if edad >= 18:
    print("podes pasar")
else:
    print("no podes pasar")
    
# VEAMOS OTRO EJEMPLO    
    
contraseña_almacenada = 'Daniel_Henao'
contraseña_escrita= 'Daniel_Henao'

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESION....")
else:
    print("CONTRASEÑA EQUIVOCADA")