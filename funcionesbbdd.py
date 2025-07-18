"""Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos. La tabla 
'productos' debe contener las siguientes columnas:

'id': Identificador único del producto (clave primaria, autoincremental).

'nombre': Nombre del producto (texto, no nulo).

'descripcion': Breve descripción del producto (texto).

'cantidad': Cantidad disponible del producto (entero, no nulo).

'precio': Precio del producto (real, no nulo).

'categoria': Categoría a la que pertenece el producto (texto)."""


#create database inventario
import sqlite3

# Conexión (se crea el archivo si no existe)
conexion = sqlite3.connect('inventario.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
''')

# Confirmar cambios y cerrar conexión
conexion.commit()
conexion.close()

print("Base de datos y tabla 'productos' creadas con éxito.")