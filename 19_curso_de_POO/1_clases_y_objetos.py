# FORMA NO OPTIMA DE CREAR OBJETOS 

# celular1_marca = "Samsung"
# celular2_marca = "Apple"
# celular3_marca = "Huawei3"

# celular1_modelo = "S23"
# celular2_modelo = "Iphone 15"
# celular3_modelo = "P20 pro"

# celular1_camaraT = "48mp"
# celular2_camaraT = "48mp"
# celular3_camaraT = "12mp"

# celular1_camaraF = "24mp"
# celular2_camaraF = "24mp"
# celular3_camaraF = "8mp"

# print(celular1_camaraF)

# """ ----------------------------- FORMA CON CLASES Y OBJETOS ------------------------------------ """

# Creemos (CLASES Y OBJETOS) con (ATRIBUTOS ESTATICOS)

# Para trabajar con clases utilizamos PascalCase

# Creamos la clase
class Celular():
    # Atributos estaticos
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'
    
# creamos un objeto que a su vez seria una instancia de la clase(Una instancia es cuando creamos un objeto de la clase)
celular1 = Celular()
# Imprimimos 
print(celular1.marca)