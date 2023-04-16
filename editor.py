import pandas as pd

import csv_manipulation

csv_manipulation.imprimir_csv('archivo.csv')

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('archivo.csv', encoding='ISO-8859-1')

# Aplica la función extraer_identificador_carretera a cada elemento en la columna "CARRETERA"
df['IS_CARR'] = df['CARRETERA'].apply(csv_manipulation.extraer_identificador_carretera)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('archivo_modificado.csv', index=False)

csv_manipulation.imprimir_csv('archivo_modificado.csv')
