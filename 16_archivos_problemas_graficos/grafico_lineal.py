import pandas as pd 
# Debemos instalar la libreria(py -m pip install matplotlib)
import matplotlib.pyplot as plt
# Debemos instalar (py -m pip install seaborn)
import seaborn as sns 

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
# Creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)
# Poniendo un punto el monmento mas alto de la actividad
plt.plot("01-09",17,"o")
# Mostrando el grafico
plt.show()
