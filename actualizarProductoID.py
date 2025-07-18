#Actualizar datos de productos, mediante su ID.import sqlite3

import sqlite3
def actualizar_producto():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    try:
        producto_id = int(input("Ingrese el ID del producto que desea actualizar: "))
    except ValueError:
        print(" ID inválido.")
        return

    # Buscar el producto
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()

    if not producto:
        print(" No se encontró un producto con ese ID.")
        return

    # Mostrar datos actuales
    print("\n=== Datos actuales del producto ===")
    print(f"ID: {producto[0]}")
    print(f"Nombre: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Cantidad: {producto[3]}")
    print(f"Precio: {producto[4]}")
    print(f"Categoría: {producto[5]}")

    # Ingresar nuevos datos (dejar en blanco para mantener)
    nuevo_nombre = input(f"Nuevo nombre [{producto[1]}]: ") or producto[1]
    nueva_descripcion = input(f"Nueva descripción [{producto[2]}]: ") or producto[2]

    while True:
        nueva_cantidad = input(f"Nueva cantidad [{producto[3]}]: ") or str(producto[3])
        if nueva_cantidad.isdigit():
            nueva_cantidad = int(nueva_cantidad)
            break
        print(" Debe ingresar un número entero.")

    while True:
        nuevo_precio = input(f"Nuevo precio [{producto[4]}]: ") or str(producto[4])
        try:
            nuevo_precio = float(nuevo_precio)
            break
        except ValueError:
            print(" Debe ingresar un número válido.")

    nueva_categoria = input(f"Nueva categoría [{producto[5]}]: ") or producto[5]

    # Actualizar en la base
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    """, (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, producto_id))

    conexion.commit()
    conexion.close()
    print(" Producto actualizado correctamente.")

# Ejecutar
#actualizar_producto()
