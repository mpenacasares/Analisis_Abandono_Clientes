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

        sns.histplot(df[col], kde=True, ax=axes[fila, columna], color="turquoise")
        axes[fila, columna].set_title(f"Distribucion de {col}")

    plt.tight_layout()

    # Guardar el grafico en formato .jpg
    ruta_imagen = os.path.join(ruta_guardado, "distribucion_numericas.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.close()
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

    plt.close()
    print(f"✅ Boxplots guardados en {ruta_imagen}")


def generar_piecharts(df, columnas_categoricas, ruta_guardado):
    """
    Genera y guarda una imagen .jpg de los piecharts para las variables categoricas definidas en variables.py
    Crea carpeta de guardado si no existe

    Parametros:
        df (pd.DataFrame): DataFrame con los datos.
        columnas_categoricas (list): Lista de 5 columnas categoricas a graficar.
        ruta_guardado (str): Ruta donde se guardara la imagen.

    Retorna:
        None
    """
    # Crear la carpeta si no existe
    os.makedirs(ruta_guardado, exist_ok=True)

    # Definir colores
    colors = ["#FFB3BA", "#BAE1FF", "#BAFFC9"]

    # Crear figura con 2 filas y 3 columnas
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))

    for i, col in enumerate(columnas_categoricas):
        fila = i // 3  # Calcular la fila correspondiente
        columna = i % 3  # Calcular la columna correspondiente

        df[col].value_counts(normalize=True).plot.pie(
            autopct="%1.1f%%",
            startangle=90,
            colors=colors[: len(df[col].unique())],  # Usamos solo 3 colores
            textprops={"fontsize": 10},
            wedgeprops={"edgecolor": "black", "linewidth": 0.5},
            ax=axes[fila, columna],
        )

        axes[fila, columna].set_title(
            f"Distribución de clientes por {col.capitalize()}"
        )
        axes[fila, columna].set_ylabel("")

    # Eliminar la última celda vacía (solo hay 5 gráficos)
    fig.delaxes(axes[1, 2])

    plt.tight_layout()

    # Guardar el grafico en formato .jpg
    ruta_imagen = os.path.join(ruta_guardado, "piecharts_categoricas.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.close()
    print(f"✅ Pie charts guardados en {ruta_imagen}")


def comparar_estadisticas(df_si, df_no):
    """
    Obtiene y compara las estadisticas descriptivas de clientes que han abandonado alguna vez el banco vs los que no.

    Parametros:
    df_si (DataFrame): Clientes que han abandonado alguna vez.
    df_no (DataFrame): Clientes que nunca han abandonado.

    Retorna:
    Muestra las estadisticas descriptivas de ambos grupos.
    """
    stats_si = df_si[va.var_clave_abandono].describe()
    stats_no = df_no[va.var_clave_abandono].describe()

    # Mostrar resultados en tablas
    print(stats_si)(name="Estadisticas Abandono Si", dataframe=stats_si)
    print(stats_si)(name="Estadisticas Abandono No", dataframe=stats_no)


def generar_boxplot_abandono(df_si, df_no, variable, ruta_guardado):
    """
    Genera y guarda un boxplot comparando clientes que han abandonado vs. los que no.

    Parametros:
        df_si (pd.DataFrame): Clientes que han abandonado al menos una vez.
        df_no (pd.DataFrame): Clientes que nunca han abandonado.
        variable (str): Nombre de la variable a graficar.
        ruta_guardado (str): Carpeta donde se guardaran las imagenes.

    Retorna:
        None: Muestra y guarda el boxplot comparativo.
    """
    # Crear carpeta si no existe
    os.makedirs(ruta_guardado, exist_ok=True)

    # Reformatear los datos en un solo DataFrame para Seaborn
    df_si["abandono"] = "Si"
    df_no["abandono"] = "No"
    df_consolidado = pd.concat(
        [df_si[[variable, "abandono"]], df_no[[variable, "abandono"]]]
    )

    # Crear la figura
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        x="abandono",
        y=variable,
        data=df_consolidado,
        hue="abandono",
        palette={"Si": "lightcoral", "No": "turquoise"},
        legend=False,
    )
    plt.title(f"Boxplot de {variable} según abandono")

    # Guardar el gráfico
    ruta_imagen = os.path.join(ruta_guardado, f"boxplot_abandono_{variable}.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.close()
    print(f"✅ Boxplot de {variable} guardado en {ruta_imagen}")


def generar_grafico_barras(df_si, df_no, variable, ruta_guardado):
    """
    Genera y guarda un grafico de barras comparando la distribucion de una variable categorica
    en clientes que han abandonado vs los que no.

    Parametros:
        df_si (pd.DataFrame): DataFrame de clientes que han abandonado al menos una vez.
        df_no (pd.DataFrame): DataFrame de clientes que nunca han abandonado.
        variable (str): Nombre de la variable a graficar.
        ruta_guardado (str): Carpeta donde se guardaran las imagenes.

    Retorna:
        None: Muestra y guarda el grafico de barras comparativo.
    """
    # Crear carpeta si no existe
    os.makedirs(ruta_guardado, exist_ok=True)

    # Reformatear los datos en un solo DataFrame para Seaborn
    df_si["abandono"] = "Si"
    df_no["abandono"] = "No"
    df_consolidado = pd.concat(
        [df_si[[variable, "abandono"]], df_no[[variable, "abandono"]]]
    )

    # Crear figura
    plt.figure(figsize=(8, 6))
    sns.countplot(
        data=df_consolidado,
        x=variable,
        hue="abandono",
        palette={"Si": "lightcoral", "No": "turquoise"},
    )

    plt.title(f"Distribución de {variable} según abandono")
    plt.xlabel(variable)
    plt.ylabel("Número de clientes")

    # Guardar el gráfico
    ruta_imagen = os.path.join(ruta_guardado, f"barras_abandono_{variable}.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.close()
    print(f"✅ Gráfico de barras de {variable} guardado en {ruta_imagen}")


def generar_histograma_abandono(df_si, df_no, variable, ruta_guardado, bins=10):
    """
    Genera y guarda un histograma comparando la distribucion de una variable numerica
    en clientes que han abandonado vs. los que no.

    Parametros:
        df_si (pd.DataFrame): Clientes que han abandonado alguna vez.
        df_no (pd.DataFrame): Clientes que nunca han abandonado.
        variable (str): Nombre de la variable numerica a graficar.
        ruta_guardado (str): Carpeta donde se guardara la imagen.
        bins (int): Numero de intervalos para agrupar los valores.

    Retorna:
        None: Muestra y guarda el histograma.
    """
    os.makedirs(ruta_guardado, exist_ok=True)  # Crear carpeta si no existe

    # Crear figura
    plt.figure(figsize=(8, 6))

    # Histograma de los clientes que han abandonado (rojo más visible)
    sns.histplot(
        df_si[variable],
        bins=bins,
        color="lightcoral",
        label="Abandono = Si",
        alpha=1,
        kde=True,
        edgecolor="black",
        linewidth=1.2,
    )

    # Histograma de los clientes que nunca han abandonado (turquesa)
    sns.histplot(
        df_no[variable],
        bins=bins,
        color="turquoise",
        label="Abandono = No",
        alpha=0.6,
        kde=True,
        edgecolor="black",
        linewidth=1.2,
    )

    # Configuración del gráfico
    plt.title(f"Distribución de {variable} según abandono")
    plt.xlabel(variable)
    plt.ylabel("Número de clientes")
    plt.legend()

    # Guardar el gráfico
    ruta_imagen = os.path.join(ruta_guardado, f"histograma_abandono_{variable}.jpg")
    plt.savefig(ruta_imagen, bbox_inches="tight", pad_inches=0.2, format="jpg", dpi=300)

    plt.close()
    print(f"✅ Histograma de {variable} guardado en {ruta_imagen}")
