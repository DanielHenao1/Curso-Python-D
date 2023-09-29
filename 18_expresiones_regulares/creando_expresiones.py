import re

# Detectando un numero CABA y ocultandolo

texto = 'Hola pedro, mi numero es: +54 11 4321-4321'

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

reemplazarlo = re.sub(pattern,'(numero oculto en texto)',texto)

print(reemplazarlo)