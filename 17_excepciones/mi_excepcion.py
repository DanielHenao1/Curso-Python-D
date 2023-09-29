# Creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f'Impresionante, cometiste el siguiente error: {err}')
        
# Lanzando mi propia excepcion
# raise MiExcepcion('jajajaja, persona poco culta')        
     
# Manejandola     
try:
    raise MiExcepcion('persona poco culta')
except:
    print('como vas a cometer ese error')