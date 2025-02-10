import os
from src import eda
from src import variables as va
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generar_histogramas_kde(df, ruta_guardado):
    """
    Genera histogramas con KDE para las variables numericas clave definidas en variables.py.
    Crea carpeta de guardado si no existe

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.
        ruta_guardado (str): Ruta donde se guardaran las imagenes.

    Retorna:
        None: Muestra y guarda los graficos.
    """
    # Crear la carpeta si no existe
    os.makedirs(ruta_guardado, exist_ok=True)

    # Crear figura con 2 filas y 3 columnas
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))

    # Recorrer variables y asignarlas a la matriz de subgraficos (2x3)
    for i, col in enumerate(va.var_numericas):
        fila = i // 3  # Calculo de fila
        columna = i % 3  # Calculo de columna
        
        sns.histplot(df[col], kde=True, ax=axes[fila, columna], color="darkblue")
        axes[fila, columna].set_title(f"Distribucion de {col}")

    plt.tight_layout()

    # Guardar el grafico en formato .jpg
    ruta_imagen = os.path.join(ruta_guardado, "distribucion_numericas.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.show()
    print(f"✅ Histogramas guardados en {ruta_imagen}")


def generar_boxplots(df, ruta_guardado):
    """
    Genera y guarda una imagen .jpg de los boxplots para las variables numericas definidas en variables.py
    Crea carpeta de guardado si no existe

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.
        ruta_guardado (str): Ruta donde se guardaran las imagenes.

    Retorna:
        None: Muestra los boxplots de las variables numericas en un formato alineado.
    """
    # Crear la carpeta si no existe
    os.makedirs(ruta_guardado, exist_ok=True)

    # Crear figura con 2 filas y 3 columnas
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))

    # Generar cada boxplot
    for i, col in enumerate(va.var_numericas):
        fila = i // 3  # Calculo de fila
        columna = i % 3  # Calculo de columna
        
        sns.boxplot(y=df[col], color="turquoise", ax=axes[fila, columna])
        axes[fila, columna].set_title(f"Boxplot de {col}")

    plt.subplots_adjust(wspace=0.4)  # Aumentar espacio entre graficas

    # Guardar el grafico en formato .jpg
    ruta_imagen = os.path.join(ruta_guardado, "boxplots_var_numericas.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.show()
    print(f"✅ Boxplots guardados en {ruta_imagen}")
