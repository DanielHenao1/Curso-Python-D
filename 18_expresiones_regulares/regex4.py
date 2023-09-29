import re

email = 'example@exxample.com'

patttern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9. -]+\.[a-zA-Z]{2,}$'

resultado = re.match(patttern, email)

if resultado:
    print('Direccion de correo valida')
else:
    print('direccion de correo invalida')    
