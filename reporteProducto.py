#Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.

import sqlite3

def reporte_bajo_stock():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    print("=== Reporte de productos con bajo stock ===")
    try:
        limite = int(input("Ingrese el límite inferior de stock (cantidad): "))
    except ValueError:
        print("⚠️ Debe ingresar un número entero válido.")
        conexion.close()
        return

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    if productos:
        print(f"\n📦 Productos con cantidad igual o menor a {limite}:\n")
        print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
            "ID", "Nombre", "Cantidad", "Precio", "Categoría", "Descripción"))
        print("-" * 80)
        for prod in productos:
            id, nombre, descripcion, cantidad, precio, categoria = prod
            print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
                id, nombre, cantidad, precio, categoria, descripcion[:20]))
    else:
        print(f"✅ No hay productos con stock igual o inferior a {limite}.")

    conexion.close()

# Ejecutar
#reporte_bajo_stock()
