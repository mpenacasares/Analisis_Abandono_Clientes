# Diccionario para renombrar columnas
columnas_renombradas = {
    "customer_id": "id_cliente",
    "credit_score": "puntacion_credito",
    "country": "pais",
    "gender": "genero",
    "age": "edad",
    "tenure": "antiguedad",
    "balance": "saldo",
    "products_number": "num_productos",
    "credit_card": "tarjeta_credito",
    "active_member": "miembro_activo",
    "estimated_salary": "salario_estimado",
    "churn": "abandono",
}

# Diccionario para convertir valores binarios a 'Si' y 'No'
mapeo_binario = {1: "Si", 0: "No"}

# Columnas con valores binarios a transformar
columnas_binarias = ["tarjeta_credito", "miembro_activo", "abandono"]

# Diccionario para traducir valores de variables categoricas
traduccion_categoricas = {
    "pais": {"France": "Francia", "Spain": "España", "Germany": "Alemania"},
    "genero": {"Male": "Hombre", "Female": "Mujer"},
}

# Variables categoricas a analizar
var_categoricas = [
    "pais",
    "genero",
    "tarjeta_credito",
    "miembro_activo",
    "abandono",
]

# Variables numericas a analizar
var_numericas = [
    "puntacion_credito",
    "edad",
    "saldo",
    "salario_estimado",
    "antiguedad",
    "num_productos",
]

# Variables clave para analisis del abandono
var_clave_abandono = [
    "edad",
    "puntacion_credito",
    "pais",
    "num_productos",
    "saldo",
    "miembro_activo",
    "tarjeta_credito",
]

# Query de soporte para la creacion de la bbdd
query_crear_tabla = """
CREATE TABLE IF NOT EXISTS BlueBank_Clientes (
    id_cliente BIGINT PRIMARY KEY,
    puntacion_credito INT,
    pais VARCHAR(50),
    genero VARCHAR(10),
    edad INT,
    antiguedad INT,
    saldo FLOAT,
    num_productos INT,
    tarjeta_credito VARCHAR(2),
    miembro_activo VARCHAR(2),
    salario_estimado FLOAT,
    abandono VARCHAR(2)
);
"""

# Query de soporte para la insercion de valores en la bbdd
query_insertar_datos = """
INSERT INTO BlueBank_Clientes (id_cliente, puntacion_credito, pais, genero, edad, antiguedad, saldo, num_productos, tarjeta_credito, miembro_activo, salario_estimado, abandono)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
