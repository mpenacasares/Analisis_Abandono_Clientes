import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src import variables as va


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


def generar_boxplots(df):
    """
    Genera boxplots para las variables numericas definidas en variables.py en una sola fila con separacion.

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.

    Retorna:
        None: Muestra los boxplots de las variables numericas en un formato alineado.
    """
    fig, axes = plt.subplots(
        nrows=1, ncols=len(va.variables_numericas), figsize=(20, 5)
    )  # 1 fila, 4 columnas

    # Generar cada boxplot
    for i, col in enumerate(va.variables_numericas):
        sns.boxplot(y=df[col], color="turquoise", ax=axes[i])
        axes[i].set_title(f"Boxplot de {col}")

    plt.subplots_adjust(wspace=0.4)  # Aumentar espacio entre graficas
    plt.show()
