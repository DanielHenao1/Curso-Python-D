# 2 listas, una con nombres otra con apellidos 
nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","tarado"]

# Registrar la informacion en un txt de forma optima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w")as file:
    file.writelines("Los datos son:\n\n")
    
    # Forma de hacer (for) con una sola linea 
    [file.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    
    # Tambien podemos hacer loo mismo con el siguiente (for)
    # for n,a in zip(nombres,apellidos):
    #     file.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n")