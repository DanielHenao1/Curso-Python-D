# with open("archivos\\texto_de_dalto.txt", 'r') as archivo:
#     for linea in archivo:
#         print("\n==== char ====")
#         print(linea)
        
        
# with open("archivos\\texto_de_dalto.txt") as archivo:   
#     print(archivo.read())          
    
    
with open("archivos\\texto_de_dalto.txt", 'w') as archivo: 
    # Sobre escibiendo el archivo(esto es muy delicado por que podemos borrar todos los datos de un archivo)
    # Tambien si el archivo no esta creado, se crea automaticamente
    archivo.writelines(["DIOS es mi pastor nada me faltara","\nmisericordioso"])   