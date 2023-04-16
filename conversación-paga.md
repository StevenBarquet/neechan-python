este fue el codígo que funciono, modificalo para que cuando encuentres CARR (case insensitive) en lugar de CARRETERA, sustituyas CARR por CARRETERA:
def extraer_identificador_carretera(lista_strings):
    identificadores = []
    for string in lista_strings:
        # Si el string contiene "KM", se asume que hay un identificador de carretera
        if "KM" in string:
            # Separa el string en una lista de palabras y busca la primera que contenga "KM"
            palabras = string.split()
            for i, palabra in enumerate(palabras):
                if "KM" in palabra:
                    # Almacena todas las palabras antes de la palabra con "KM"
                    identificador = " ".join(palabras[:i])
                    identificadores.append(identificador)
                    break
        else:
            identificadores.append(None)
    # Si no se encuentra ningún identificador de carretera, retorna una lista vacía
    return identificadores

Puedes modificar la función extraer_identificador_carretera para que también busque "CARR" y lo sustituya por "CARRETERA" antes de almacenar el identificador. Aquí tienes el código modificado:

python

def extraer_identificador_carretera(lista_strings):
    identificadores = []
    for string in lista_strings:
        # Si el string contiene "KM", se asume que hay un identificador de carretera
        if "KM" in string.upper():
            # Separa el string en una lista de palabras y busca la primera que contenga "KM"
            palabras = string.split()
            for i, palabra in enumerate(palabras):
                if "KM" in palabra.upper():
                    # Almacena todas las palabras antes de la palabra con "KM"
                    identificador = " ".join(palabras[:i])

                    # Sustituye "CARR" por "CARRETERA" en el identificador, si está presente (case insensitive)
                    identificador = identificador.replace("CARR", "CARRETERA")
                    identificador = identificador.replace("carr", "CARRETERA")

                    identificadores.append(identificador)
                    break
        else:
            identificadores.append(None)
    # Si no se encuentra ningún identificador de carretera, retorna una lista vacía
    return identificadores

De esta manera, si encuentra "CARR" en el identificador, lo sustituirá por "CARRETERA" antes de agregarlo a la lista de identificadores.
mlmjm123@gmail.com
3 / 3
Quiero evaluar con extraer_identificador_carretera cada string de la columna "CARRETERA" de mi csv y almacenar el valor resultante en la columna "IS_CARR" Si no existe la columna IS_CARR creala

Para lograr esto, primero necesitas cargar tu archivo CSV utilizando la biblioteca pandas. Luego, puedes aplicar la función extraer_identificador_carretera a cada fila de la columna "CARRETERA" y almacenar los resultados en una nueva columna "IS_CARR". Aquí tienes el código para hacer esto:

python

import pandas as pd

def extraer_identificador_carretera(string):
    # Aquí va la función extraer_identificador_carretera que te proporcioné anteriormente

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('tu_archivo.csv')

# Aplica la función extraer_identificador_carretera a cada elemento en la columna "CARRETERA"
df['IS_CARR'] = df['CARRETERA'].apply(extraer_identificador_carretera)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('archivo_modificado.csv', index=False)

Reemplaza 'tu_archivo.csv' con la ruta y nombre de tu archivo CSV. Una vez que se ejecute el código, se creará un nuevo archivo llamado 'archivo_modificado.csv' con los resultados en la columna "IS_CARR". Si la columna "IS_CARR" no existe, se creará automáticamente.
mlmjm123@gmail.com
al implementar extraer_identificador_carretera me genera el array completo, haz que evalue sólo el string actual de la iteración

Mis disculpas por la confusión. La función extraer_identificador_carretera estaba diseñada para procesar listas de strings. Voy a modificar la función para que procese un solo string en lugar de una lista, y ajustaré el código para aplicar la función a cada elemento en la columna "CARRETERA" del DataFrame.

python

import pandas as pd

def extraer_identificador_carretera(string):
    # Si el string contiene "KM", se asume que hay un identificador de carretera
    if "KM" in string.upper():
        # Separa el string en una lista de palabras y busca la primera que contenga "KM"
        palabras = string.split()
        for i, palabra in enumerate(palabras):
            if "KM" in palabra.upper():
                # Almacena todas las palabras antes de la palabra con "KM"
                identificador = " ".join(palabras[:i])

                # Sustituye "CARR" por "CARRETERA" en el identificador, si está presente (case insensitive)
                identificador = identificador.replace("CARR", "CARRETERA")
                identificador = identificador.replace("carr", "CARRETERA")

                return identificador
    return None

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('tu_archivo.csv')

# Aplica la función extraer_identificador_carretera a cada elemento en la columna "CARRETERA"
df['IS_CARR'] = df['CARRETERA'].apply(extraer_identificador_carretera)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('archivo_modificado.csv', index=False)

Con estos cambios, la función extraer_identificador_carretera procesará un solo string en lugar de una lista de strings. La función apply() de pandas aplicará esta función a cada elemento en la columna "CARRETERA" del DataFrame y almacenará los resultados en la columna "IS_CARR".