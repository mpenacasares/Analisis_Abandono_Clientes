# %% #  PDTE: BORRAR DESPUES PRINT Y COMENTARIOS, MAIN LIMPIO
from src import eda
from src import transformacion as tr
from src import carga as ca
from src import variables as va

# TEST EDA ✔

df = eda.extraer_datos_csv("datos/bruto/Bank_Customer_Churn_Prediction.csv")

eda.revisar_estructura(df)

eda.get_duplicate_rows(df)

df_nulos = eda.revisar_valores_nulos(df)

eda.obtener_estadisticas(df)

eda.revisar_valores_unicos(df)

# TEST TRANSFORMACION - WIP
df.rename(columns=va.columnas_renombradas, inplace=True)

df = tr.transformar_binarios(df, va.columnas_binarias)

tr.generar_boxplots(df)

# %%
