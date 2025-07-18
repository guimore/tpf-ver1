#Visualizar datos de los productos registrados.

import sqlite3

def mostrar_productos():
    # Conexión a la base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    # Consultar productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print("⚠️ No hay productos registrados.")
    else:
        print("\n=== Listado de Productos ===")
        print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
            "ID", "Nombre", "Cantidad", "Precio", "Categoría", "Descripción"))
        print("-" * 80)
        for prod in productos:
            id, nombre, descripcion, cantidad, precio, categoria = prod
            print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
                id, nombre, cantidad, precio, categoria, descripcion[:20]))

    # Cerrar conexión
    conexion.close()

# Ejecutar
#mostrar_productos()
