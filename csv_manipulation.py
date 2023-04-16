import pandas as pd

def imprimir_csv(ruta):
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')
    print(datos)


def mover_columnas(ruta):
    datos = pd.read_csv(ruta, encoding='ISO-8859-1')
    print(datos)
