import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src import variables as va


def extraer_datos_csv(ruta):
    """
    Extrae un archivo CSV en un DataFrame de Pandas y muestra sus primeras filas.

    Parametros:
        ruta (str): Ruta del archivo CSV a extraer.

    Retorna:
        pd.DataFrame: DataFrame con los datos extraidos.
    """
    if not os.path.exists(ruta):
        print(f"⚠ Error: El archivo '{ruta}' no existe.")
        return None  # Retornar None si el archivo no existe

    try:
        df = pd.read_csv(ruta)
        print(
            f"✅ Datos extraidos correctamente. Filas: {df.shape[0]}, Columnas: {df.shape[1]}"
        )
        print(df.head())  # Mostrar las primeras filas
        return df
    except (
        Exception
    ) as e:  # Capturar posibles errores inesperados y guardarlos en la variable e
        print(f"⚠ Error al extraer el archivo: {e}")
        return None


def revisar_estructura(df):
    """
    Muestra informacion basica sobre la estructura del DataFrame.

    Parametros:
        df (pd.DataFrame): DataFrame a analizar.

    Retorna:
        None
    """
    print("📌 Dimensiones del dataset:")
    print(f"  - Filas: {df.shape[0]}")
    print(f"  - Columnas: {df.shape[1]}\n")

    print("📌 Nombres de las columnas:")
    print(df.columns.tolist(), "\n")

    print("📌 Tipos de datos:")
    print(df.dtypes, "\n")

    # Identificar duplicados
    duplicados = df.duplicated().sum()
    print(
        f"📌 Datos duplicados: {duplicados} ({round(duplicados / df.shape[0] * 100, 2)}%)\n"
    )


def get_duplicate_rows(df):
    """
    Encuentra y devuelve las filas duplicadas completas de un DataFrame.

    Parametros:
        df (pd.DataFrame): DataFrame de entrada.

    Retorna:
        pd.DataFrame: DataFrame con las filas duplicadas.
    """
    duplicate_rows = df[df.duplicated(keep=False)]

    if duplicate_rows.empty:
        print("✅ No hay filas duplicadas en el dataset.")
    else:
        print(f"⚠ Hay {duplicate_rows.shape[0]} filas duplicadas en el dataset.")
        print(duplicate_rows)

    return duplicate_rows


def revisar_valores_nulos(df):
    """
    Muestra la cantidad y porcentaje de valores nulos en cada columna.

    Parametros:
        df (pd.DataFrame): DataFrame a analizar.

    Retorna:
        pd.DataFrame: DataFrame con informacion sobre valores nulos.
    """
    nulos = df.isnull().sum()
    porcentaje_nulos = round((nulos / len(df)) * 100, 2)
    no_nulos = df.notna().sum()
    porcentaje_no_nulos = round((no_nulos / len(df)) * 100, 2)

    df_nulos = pd.DataFrame(
        {
            "Valores nulos": nulos,
            "% Nulos": porcentaje_nulos.astype(str)
            + "%",  # astype(str) para convertir float a str y poder concatenar con %
            "% No Nulos": porcentaje_no_nulos.astype(str) + "%",
            "Valores Unicos": df.nunique(),
            "Tipo de Dato": df.dtypes,
        }
    )

    print(
        f"📌 Columnas con valores nulos: {len(df_nulos[df_nulos['Valores nulos'] > 0])}"
    )
    print(
        f"📌 Columnas sin valores nulos: {len(df_nulos[df_nulos['Valores nulos'] == 0])}"
    )

    print(df_nulos[df_nulos["Valores nulos"] > 0])  # Muestra solo columnas con nulos

    return df_nulos


def obtener_estadisticas(df, nombre_df="Dataset"):
    """
    Muestra estadisticas descriptivas de variables numericas y categoricas.

    Parametros:
        df (pd.DataFrame): DataFrame a analizar.
        nombre_df (str, opcional): Nombre del DataFrame. Por defecto, "Dataset".

    Retorna:
        None
    """
    # Mostrar estadisticas generales con 2 decimales sin notacion cientifica
    pd.options.display.float_format = "{:.2f}".format

    print(f"📌 Estadisticas descriptivas de variables numericas de {nombre_df}:")
    print(df.describe().T)

    print(f"\n📌 Estadisticas descriptivas de variables categoricas de {nombre_df}:")
    print(df.describe(include="O").T)


def revisar_valores_unicos(df):
    """
    Muestra los valores unicos y sus frecuencias en cada variable categorica.

    Parametros:
        df (pd.DataFrame): DataFrame a analizar.

    Retorna:
        None
    """
    columnas_categoricas = df.select_dtypes(include="object").columns.tolist()

    if not columnas_categoricas:
        print("✅ No hay columnas categoricas en el dataset.")
        return

    print("📌 Analisis de valores unicos en variables categoricas:\n")

    for columna in columnas_categoricas:
        print(f"\n----------- ANALIZANDO: '{columna.upper()}' -----------\n")
        print(f"Valores unicos: {df[columna].unique()}\n")
        print(f"Frecuencia de valores:\n{df[columna].value_counts()}\n")


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


def traducir_categoricas(df):
    """
    Traduce los valores de las variables categoricas segun el diccionario en variables.py.

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.

    Retorna:
        pd.DataFrame: DataFrame con los valores traducidos.
    """
    df = df.copy()
    for col, mapping in va.traduccion_categoricas.items():
        if col in df.columns:
            df[col] = df[col].replace(mapping)
    return df
