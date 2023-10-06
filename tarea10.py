import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo problemas_del_corazon-5.csv
data = pd.read_csv('problemas_del_corazon-5.csv')

# Contar las ocurrencias de cada valor en la columna "cardiaco"
cardiaco_counts = data['cardiaco'].value_counts()

# Crear un diagrama de sectores
plt.figure(figsize=(6, 6))
plt.pie(cardiaco_counts, labels=cardiaco_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Diagrama de Sectores de Cardiacos')

# Mostrar el diagrama de sectores
plt.tight_layout()
plt.show()
