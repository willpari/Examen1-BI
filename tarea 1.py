import matplotlib.pyplot as plt

# Datos del País Perú
x = [2012, 2022, 2025, 2028]  # años
y = [42, 43, 45, 47]  # población

# Datos del País Colombia
x2 = [2012, 2022, 2025, 2028]  # años
y2 = [42, 48, 49, 50]  # población

# Crear el gráfico
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.plot(x, y, label='Perú', color='blue', marker='o')  # Gráfico de Perú en azul
plt.plot(x2, y2, label='Colombia', color='green', marker='s')  # Gráfico de Colombia en verde

# Etiquetas y título
plt.xlabel('Años')
plt.ylabel('Población')
plt.title('Población de Perú y Colombia (2012-2028)')

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
