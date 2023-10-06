import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo salario.csv
data = pd.read_csv('salario.csv')

# Seleccionar las columnas de "edad" y "estudio"
edad = data['edad']
estudio = data['estudio']

# Crear un gráfico de dispersión (scatter plot) para visualizar la relación
plt.figure(figsize=(10, 6))
plt.scatter(edad, estudio, alpha=0.5)
plt.xlabel('Edad')
plt.ylabel('Nivel de Estudio')
plt.title('Relación entre Edad y Nivel de Estudio')
plt.grid(True)

# Mostrar el gráfico
plt.show()
