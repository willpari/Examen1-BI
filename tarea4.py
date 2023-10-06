import pandas as pd

# Cargar los datos desde el archivo problemas_del_corazon.csv
data = pd.read_csv('problemas_del_corazon.csv')

# Calcular la matriz de correlaciones de Spearman
correlation_matrix = data.corr(method='spearman')

# Mostrar la matriz de correlaciones
print(correlation_matrix)
