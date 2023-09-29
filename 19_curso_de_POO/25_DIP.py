# class Diccionario:
#     def verificar_palabra(self, palabra):
#         # Logica para verificar palabras
#         pass

# class CorreccionOrtografico:
#     def __init__(self,):    
#         self.diccionario = Diccionario()  
        
#     def corregir_texto(self, texto):
#         # Usamos el diccionario para corregir el texto 
#         pass


# Lo anterior lo debemos hacer de la siguiente manera     
              
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica patra verificar palabra si esta en el diccionario   
        pass
    
# class ServicioOnline(VerificadorOrtografico):
#     def verificar_palabra(self, palabra):
#         # Logica para verificar palabras desde el servicio web
#         pass
        
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador 
        
    def corregir_texto(self, texto):
        # Usamos el verificador para corregir texto
        
     
               
         
   