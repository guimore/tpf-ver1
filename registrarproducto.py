import sqlite3

def registrar_producto():
    # Conexión a la base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    # Solicitar datos al usuario
    print("=== Registrar nuevo producto ===")
    nombre = input("Nombre del producto: ").strip()
    descripcion = input("Descripción: ").strip()
    
    while True:
        try:
            cantidad = int(input("Cantidad disponible: "))
            break
        except ValueError:
            print(" Ingrese un número entero válido para la cantidad.")
    
    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError:
            print(" Ingrese un número válido para el precio.")

    categoria = input("Categoría: ").strip()

    # Insertar en la base de datos
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))

    # Guardar y cerrar
    conexion.commit()
    conexion.close()
    print(" Producto registrado con éxito.")

# Ejecutar
#registrar_producto()
