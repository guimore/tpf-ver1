#Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre 
#o categoría

import sqlite3

def buscar_productos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    print("=== Buscar Productos ===")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    opcion = input("Seleccione una opción (1/2/3): ").strip()

    if opcion == "1":
        try:
            producto_id = int(input("Ingrese el ID del producto: "))
            cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        except ValueError:
            print(" ID inválido.")
            conexion.close()
            return

    elif opcion == "2":
        nombre = input("Ingrese el nombre (o parte del nombre): ").strip()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))

    elif opcion == "3":
        categoria = input("Ingrese la categoría: ").strip()
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{categoria}%",))
    
    else:
        print(" Opción no válida.")
        conexion.close()
        return

    resultados = cursor.fetchall()

    if resultados:
        print("\n=== Resultados encontrados ===")
        print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
            "ID", "Nombre", "Cantidad", "Precio", "Categoría", "Descripción"))
        print("-" * 80)
        for prod in resultados:
            id, nombre, descripcion, cantidad, precio, categoria = prod
            print("{:<5} {:<20} {:<10} {:<8} {:<10} {:<20}".format(
                id, nombre, cantidad, precio, categoria, descripcion[:20]))
    else:
        print("🔎 No se encontraron resultados con ese criterio.")

    conexion.close()

# Ejecutar
#buscar_productos()
