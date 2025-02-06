import os
import pandas as pd


def cargar_datos_csv(ruta):
    """
    Carga un archivo CSV en un DataFrame de Pandas y muestra sus primeras filas.

    Parametros:
        ruta (str): Ruta del archivo CSV a cargar.

    Retorna:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    if not os.path.exists(ruta):
        print(f"⚠ Error: El archivo '{ruta}' no existe.")
        return None  # Retornar None si el archivo no existe

    try:
        df = pd.read_csv(ruta)
        print(
            f"✅ Datos cargados correctamente. Filas: {df.shape[0]}, Columnas: {df.shape[1]}"
        )
        display(df.head())  # Mostrar las primeras filas
        return df
    except (
        Exception
    ) as e:  # Capturar posibles errores inesperados y guardarlos en la variable e
        print(f"⚠ Error al cargar el archivo: {e}")
        return None
