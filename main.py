# %% #  PDTE: BORRAR DESPUES PRINT Y COMENTARIOS, MAIN LIMPIO
from src import eda
from src import analisis as an
from src import carga as ca
from src import variables as va
import pandas as pd

## EDA INICIAL OK
print(f"EDA INICIAL ✨")
df = eda.extraer_datos_csv("datos/bruto/Bank_Customer_Churn_Prediction.csv")

eda.revisar_estructura(df)

eda.get_duplicate_rows(df)

df_nulos = eda.revisar_valores_nulos(df)

eda.revisar_valores_unicos(df)

df.rename(columns=va.columnas_renombradas, inplace=True)

df = eda.transformar_binarios(df, va.columnas_binarias)

eda.obtener_estadisticas(df)

df.to_csv("datos/procesado/EDA_Bank_Customer_Churn_Prediction.csv", index=False)

print(f"Analisis perfil cliente general ✨")

an.generar_histogramas_kde(df, ruta_guardado="imagenes/")

an.generar_boxplots(df, ruta_guardado="imagenes/")

# %%
