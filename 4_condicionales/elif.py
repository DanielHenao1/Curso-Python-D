
ingreso_mensual = 500

if ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo")
    
# (elif) LO UTILIZAMOS PARA EVALUAR MAS DE UNA CONDICION ANTES DE QUE INGRESE AL ELSE    
    
elif ingreso_mensual > 2000:
    print("Estas bien en latinoamerica")

elif ingreso_mensual > 1500:
    print("Estas bien en colombia")

elif ingreso_mensual > 1000:
    print("Estas bien en argentina")

    
else:
    print("sos de recursos bajos")    
        
        
# ACONTINUACION VERERMOS UN EJEMPLO DE IF ANIDADO O (IF dentro de otro IF)        

ingreso_mensual1 = 12000
gasto_mensual = 8000

if ingreso_mensual1 > 10000:
    if ingreso_mensual1 - gasto_mensual > 3000:
        print("ahora si estas bien")
    else:
        print("estas gastando mucho dinero, no te va alcanzar")
        

# VEAMOS OTRO EJEMPLO MAS COMPLEJO (if anidados y else if (elif))

ingreso_mensual1 = 10100
gasto_mensual = 10101

if ingreso_mensual1 > 10000:
    if ingreso_mensual1 - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual1 - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("Amigo estas gastando mucho dinero, no te va alcanzar")