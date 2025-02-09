# %% #  PDTE: BORRAR DESPUES PRINT Y COMENTARIOS, MAIN LIMPIO
from src import eda
from src import analisis as an
from src import carga as ca
from src import variables as va

## EDA INICIAL OK
df = eda.extraer_datos_csv("datos/bruto/Bank_Customer_Churn_Prediction.csv")

eda.revisar_estructura(df)

eda.get_duplicate_rows(df)

df_nulos = eda.revisar_valores_nulos(df)

eda.obtener_estadisticas(df)

eda.revisar_valores_unicos(df)

df.rename(columns=va.columnas_renombradas, inplace=True)

df = eda.transformar_binarios(df, va.columnas_binarias)

eda.obtener_estadisticas(df)

df.to_csv("datos/procesado/EDA_Bank_Customer_Churn_Prediction.csv", index=False)

eda.generar_boxplots(df)

## ANALISIS

# %%
