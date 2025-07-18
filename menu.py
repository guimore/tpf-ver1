from colorama import init, Fore
from registrarproducto import registrar_producto
from visualizarProductos import mostrar_productos
from buscarProducto import buscar_productos
from actualizarProductoID import actualizar_producto
from eliminarProductoID import eliminar_producto
from reporteProducto import reporte_bajo_stock
 
# Inicializar colorama
init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN + "\n=== MENÚ PRINCIPAL ===")
        print(Fore.YELLOW + "1. Registrar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto (por ID, nombre o categoría)")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Reporte de productos con bajo stock")
        print(Fore.RED + "7. Salir")

        opcion = input(Fore.CYAN + "Seleccione una opción (1-7): ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_productos()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.GREEN + " Hasta luego.")
            break
        else:
            print(Fore.RED + " Opción inválida. Intente de nuevo.")

# Llamar al menú
#menu()
if __name__ == "__main__":
    menu()