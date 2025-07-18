#Eliminación de productos, mediante su ID.

import sqlite3

def eliminar_producto():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    try:
        producto_id = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("⚠️ ID inválido.")
        return

    # Buscar el producto
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()

    if not producto:
        print("❌ No se encontró un producto con ese ID.")
        return

    # Mostrar datos del producto
    print("\n=== Producto encontrado ===")
    print(f"ID: {producto[0]}")
    print(f"Nombre: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Cantidad: {producto[3]}")
    print(f"Precio: {producto[4]}")
    print(f"Categoría: {producto[5]}")

    confirmacion = input("\n¿Está seguro que desea eliminar este producto? (s/n): ").lower()
    if confirmacion == 's':
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conexion.commit()
        print("✅ Producto eliminado correctamente.")
    else:
        print("❎ Operación cancelada.")

    conexion.close()

# Ejecutar
#eliminar_produc_
