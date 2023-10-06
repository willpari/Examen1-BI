import pandas as pd

# Cargar los datos desde el archivo problemas_del_corazon-2.csv
data = pd.read_csv('problemas_del_corazon-2.csv')

# Calcular la correlación de Spearman entre "presion" y "colesterol"
correlation = data['presion'].corr(data['colesterol'], method='spearman')

# Mostrar el valor de la correlación de Spearman
print(correlation)
