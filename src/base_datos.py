import mysql.connector
import os
from dotenv import load_dotenv
from src import variables as va

# Cargar las variables del archivo .env
load_dotenv()

def conectar_mysql():
    """
    Establece la conexion con MySQL y devuelve el objeto de conexion.
    """
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("✅ Conexión a MySQL establecida.")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar con MySQL: {err}")
        return None


def crear_base_datos():
    """
    Crea la base de datos en MySQL si no existe.
    """
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
        print(f"✅ Base de datos '{os.getenv('DB_NAME')}' creada o ya existente.")
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print(f"❌ Error al crear la base de datos: {err}")


def crear_tabla():
    """
    Crea la tabla 'BlueBank_Clientes' en la base de datos si no existe.
    """
    conexion = conectar_mysql()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(va.query_crear_tabla)
            print("✅ Tabla 'BlueBank_Clientes' creada o ya existente.")
            cursor.close()
            conexion.close()
        except mysql.connector.Error as err:
            print(f"❌ Error al crear la tabla: {err}")


def insertar_datos(df):
    """
    Inserta los datos procesados en la tabla 'BlueBank_Clientes'.
    """
    conexion = conectar_mysql()
    if conexion:
        try:
            cursor = conexion.cursor()
            datos = df.values.tolist()
            cursor.executemany(va.query_insertar_datos, datos)
            conexion.commit()
            print("✅ Datos insertados correctamente en la tabla 'BlueBank_Clientes'.")
            cursor.close()
            conexion.close()
        except mysql.connector.Error as err:
            print(f"❌ Error al insertar datos en MySQL: {err}")
            
            
def preguntar_carga_mysql(df):
    """
    Pregunta al usuario si desea cargar los datos en MySQL.  
    Solo acepta respuestas "Si" o "No" y maneja entradas no validas.
    
    Parametros:
        df (pd.DataFrame): DataFrame con los datos procesados para cargar en MySQL.
    
    Retorna:
        None
    """
    while True:
        respuesta = input("\n¿Quieres generar la base de datos en MySQL y cargar los datos? (Si/No): ").strip().lower()
        
        if respuesta == "si":
            if crear_base_datos():  
                if insertar_datos(df):  
                    print("✅ Base de datos creada y datos cargados en MySQL correctamente.")
                else:
                    print("⚠ La base de datos fue creada, pero hubo un problema al cargar los datos.")
            else:
                print("❌ No se pudo crear la base de datos. Revisa la conexión con MySQL.")
            break  

        elif respuesta == "no":
            print("⏩ Omitiendo la carga en MySQL. Proceso finalizado.")
            break 

        else:
            print("⚠ Entrada no válida. Por favor, responde con 'Si' o 'No'.")