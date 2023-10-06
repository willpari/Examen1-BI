import pandas as pd

# Crear un diccionario con los datos
data = {
    'MES': ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL'],
    'VENTAS': [30500, 35600, 28300, 33900],
    'GASTOS': [22000, 23400, 18100, 20700]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
