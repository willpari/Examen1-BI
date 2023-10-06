import pandas as pd

# Cargar los datos desde el archivo problemas_del_corazon-1.csv
data = pd.read_csv('problemas_del_corazon-1.csv')

# Calcular la correlación de Pearson entre "edad" y "colesterol"
correlation = data['edad'].corr(data['colesterol'], method='pearson')

# Mostrar el valor de la correlación de Pearson
print(correlation)
