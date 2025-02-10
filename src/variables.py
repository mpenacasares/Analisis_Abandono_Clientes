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

# Variables numericas a analizar
var_numericas = ["puntacion_credito", "edad", "saldo", "salario_estimado", "antiguedad", "num_productos"]
