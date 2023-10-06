import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo problemas_del_corazon-3.csv
data = pd.read_csv('problemas_del_corazon-3.csv')

# Contar las ocurrencias de cada valor en la columna "diabetico"
diabetico_counts = data['diabetico'].value_counts()

# Crear un gráfico de barras
plt.figure(figsize=(8, 6))
diabetico_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Diabetico')
plt.ylabel('Cantidad')
plt.title('Cantidad de Diabéticos y No Diabéticos')
plt.xticks(rotation=0)

# Mostrar el gráfico de barras
plt.tight_layout()
plt.show()
