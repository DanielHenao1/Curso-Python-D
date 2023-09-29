import pandas as pd 
# Debemos instalar la libreria(py -m pip install matplotlib)
import matplotlib.pyplot as plt
# Debemos instalar (py -m pip install seaborn)
import seaborn as sns 

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")
# Creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

# Mostrando el grafico
plt.show()
