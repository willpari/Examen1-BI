import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo salario-1.csv
data = pd.read_csv('salario-1.csv')

# Seleccionar las columnas de "estudio" y "ingreso"
estudio = data['estudio']
ingreso = data['ingreso']

# Crear un gráfico de barras para visualizar la relación
plt.figure(figsize=(12, 6))
plt.bar(estudio, ingreso)
plt.xlabel('Nivel de Estudio')
plt.ylabel('Ingreso')
plt.title('Ingreso vs Nivel de Estudio')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejorar la legibilidad

# Mostrar el gráfico
plt.tight_layout()
plt.show()
