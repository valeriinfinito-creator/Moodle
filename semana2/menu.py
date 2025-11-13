#lista donde se guardan los productos
inventario = []

def agregar_producto():
    """Agrega un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado correctamente.\n")

def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        print("\n--- INVENTARIO ---")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print("------------------\n")

def calcular_estadisticas():
    """Calcula el valor total y la cantidad total de productos."""
    if len(inventario) == 0:
        print("📊 No hay productos para calcular.\n")
    else:
        valor_total = 0
        cantidad_total = 0
        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
            cantidad_total += producto["cantidad"]
        
        print("\n--- ESTADÍSTICAS ---")
        print(f"Valor total del inventario: ${valor_total}")
        print(f"Cantidad total de productos: {cantidad_total}")
        print("--------------------\n")

#menu principal
def menu():
    """Muestra el menú y controla las opciones."""
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Elija una opción (1-4): ")
        print()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

#inicio del programa
menu()

