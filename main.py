import matplotlib

matplotlib.use("Agg")  # Forzar backend sin interfaz gráfica
from src import eda
from src import analisis as an
from src import base_datos as bd
from src import variables as va

print(
    f"\n-------------- ✨ Hola! 😊 Bienvenido/a al análisis exploratorio de los clientes de BlueBank, empezamos! ✨--------------\n"
)

print(f"\n---------------------------- ✨ EDA inicial ✨----------------------------\n")

df = eda.extraer_datos_csv("datos/bruto/Bank_Customer_Churn_Prediction.csv")

df.rename(columns=va.columnas_renombradas, inplace=True)

df = eda.transformar_binarios(df, va.columnas_binarias)

df = eda.traducir_categoricas(df)

eda.revisar_estructura(df)

eda.get_duplicate_rows(df)

df_nulos = eda.revisar_valores_nulos(df)

eda.revisar_valores_unicos(df)

eda.obtener_estadisticas(df)

df.to_csv("datos/procesado/EDA_Bank_Customer_Churn_Prediction.csv", index=False)

print(
    f"\n---------------------------- ✨ Perfil cliente general ✨ ----------------------------\n"
)

an.generar_piecharts(df, va.var_categoricas, ruta_guardado="imagenes/")

an.generar_histogramas_kde(df, ruta_guardado="imagenes/")

an.generar_boxplots(df, ruta_guardado="imagenes/")

print(
    f"\n---------------------------- ✨ Perfil de los clientes en función de si han abandonado el banco alguna vez o no ✨ ----------------------------\n"
)
df_abandono_si = df[df["abandono"] == "Si"].copy()
df_abandono_no = df[df["abandono"] == "No"].copy()

df_abandono_si_filtrado = df_abandono_si[va.var_clave_abandono]
df_abandono_no_filtrado = df_abandono_no[va.var_clave_abandono]

eda.obtener_estadisticas(df_abandono_si_filtrado, "Clientes que han abandonado")
eda.obtener_estadisticas(df_abandono_no_filtrado, "Clientes que nunca han abandonado")

an.generar_boxplot_abandono(
    df_abandono_si, df_abandono_no, "saldo", ruta_guardado="imagenes/"
)

an.generar_grafico_barras(
    df_abandono_si, df_abandono_no, "miembro_activo", ruta_guardado="imagenes/"
)
an.generar_grafico_barras(
    df_abandono_si, df_abandono_no, "pais", ruta_guardado="imagenes/"
)

an.generar_histograma_abandono(
    df_abandono_si, df_abandono_no, "edad", ruta_guardado="imagenes/"
)

print(
    f"\n---------------------------- ✨ Creación de la base de datos y carga de datos en MySQL ✨ ----------------------------\n"
)

bd.preguntar_carga_mysql(df)
