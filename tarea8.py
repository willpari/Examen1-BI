import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo problemas_del_corazon-4.csv
data = pd.read_csv('problemas_del_corazon-4.csv')

# Seleccionar la columna "presion"
presion = data['presion']

# Crear un histograma
plt.figure(figsize=(8, 6))
plt.hist(presion, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Presión')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Presión')

# Mostrar el histograma
plt.tight_layout()
plt.show()
