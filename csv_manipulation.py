import pandas as pd

def imprimir_csv(ruta):
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')
    print(datos)


def mover_columnas(ruta, colRemove, colInsert):
    """
    Mueve una columna en un archivo CSV a una posición específica.

    Args:
        ruta (str): La ruta al archivo CSV que se va a modificar.
        colRemove (str): El nombre de la columna que se va a mover.
        colInsert (str): El nombre de la columna después de la cual se va a insertar la columna que se va a mover.

    Returns:
        None

    Raises:
        FileNotFoundError: Si el archivo CSV no se encuentra en la ruta especificada.
        ValueError: Si las columnas especificadas no existen en el archivo CSV.

    Ejemplo:
        mover_columnas('datos.csv', 'colA', 'colC')

    En este ejemplo, la función moverá la columna 'colA' a la posición después de la columna 'colC' en el archivo 'datos.csv'.
    """
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')

    cols = list(datos.columns)
    cols.remove(colRemove)
    colInsertIndex = cols.index(colInsert)   # Obtiene el índice de la columna colInsert y lo incrementa en 1 para colocar colRemove después de colInsert
    cols.insert(colInsertIndex, colRemove)

    datos = datos[cols]  # Reordena las columnas en el DataFrame según el nuevo orden

    # Guarda el archivo CSV con las columnas reordenadas
    datos.to_csv(ruta, index=False)


def agregar_columnas(ruta):
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')
    print(datos)


datos_prueba = [
    "CARR A LAGUNA DE SANCHEZ KM 32 SAN JUAN BAUTISTA",
    "CARRETERA NACIONAL KM 244 SAN JOSE NORTE",
    "CARRETERA NACIONAL KM 246+300 EL CERCADO",
    "CARRETERA NACIONAL KM 245 EL CERCADO",
    "MANUEL TAMEZ, EL CERCADO"
]

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

def obtener_col_vars(ruta, columna):
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')
    valores_columna = datos[columna].tolist()
    return valores_columna