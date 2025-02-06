# %% # Simbolo para activar opciones Run Cell, Run Below y Debug Cell
from src import eda
from src import transformacion as tr
from src import carga as ca
from src import variables as va

# Cargar un CSV
# 🚨 Comprobar ruta del archivo buscado en funcion de ubicacion de main
df = eda.extraer_datos_csv("datos/bruto/Bank_Customer_Churn_Prediction.csv")


# %%
