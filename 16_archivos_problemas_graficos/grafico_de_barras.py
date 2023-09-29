import pandas as pd 
# Debemos instalar la libreria(py -m pip install matplotlib)
import matplotlib.pyplot as plt
# Debemos instalar (py -m pip install seaborn)
import seaborn as sns 

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")
# Creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

# Obteniendo el total de ingresos 
total_ingresos = df['ingresos'].sum()

# Mostrando el total 
print(f'El total de ingresos es de: ${total_ingresos} USD.')

# Mostrando el grafico
plt.show()

