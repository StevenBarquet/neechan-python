import pandas as pd

datos = pd.read_csv('archivo.csv', encoding='ISO-8859-1')

cols = list(datos.columns)
cols.remove('ID_ATUS_UNICA')
cols.insert(cols.index('CALLE1'), 'ID_ATUS_UNICA')

datos = datos[cols]

print(datos)