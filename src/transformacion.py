import pandas as pd
from src import variables as va

# Transformación binaria
def transformar_binarios(df, columnas):
    """
    Convierte valores binarios (1 y 0) a 'Si' y 'No' respectivamente en las columnas especificadas.

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.
        columnas (list): Lista de columnas a transformar.

    Retorna:
        pd.DataFrame: DataFrame con valores transformados.
    """
    for col in columnas:
        # Verificar si la columna tiene valores binarios antes de aplicar la transformacion
        if df[col].isin([0, 1]).all():
            df[col] = df[col].map(va.mapeo_binario)
    return df
