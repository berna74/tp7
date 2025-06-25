import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv(dotenv_path="/home/martin/TP6_PWD/pwd2025-tp-6-backend-berna74/app/.env")
database_name = os.getenv("DB_NAME")

# Configuración de la base de datos
database_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT", 3306)),  # Conversión segura a entero
    'raise_on_warnings': True,
    "database": database_name
}

# Depuración de las variables de entorno
print("DB_PORT:", os.getenv("DB_PORT"))
print("database_config:", database_config)

# Definición de las tablas a eliminar
DROPPED_TB = {
    "articulos_categorias": "DROP TABLE IF EXISTS articulos_categorias;",
    "articulos": "DROP TABLE IF EXISTS articulos;",
    "proveedores": "DROP TABLE IF EXISTS proveedores;",
    "marcas": "DROP TABLE IF EXISTS marcas;",
    "categorias": "DROP TABLE IF EXISTS categorias;"
}

# Función para eliminar las tablas
def rollback_db():
    try:
        cxn = mysql.connector.connect(**database_config)
        cursor = cxn.cursor()
        for table in DROPPED_TB:
            print(f"Dropped table: {table}", end=" ")
            try:
                cursor.execute(DROPPED_TB[table])
                print('ok')
                cxn.commit()
            except Error as e:
                print(f"{e}")
        cursor.close()
        cxn.close()
    except Error as err:
        print(f"Error al conectar a la base de datos: {err}")

# Ejecutar la función de rollback
rollback_db()