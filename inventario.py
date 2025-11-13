# Se solicita el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Validación del precio como float
while True:
    # Se solicita el precio
    precio = input("Ingrese el precio: ")

    # Se valida que el precio no tenga más de un punto
    if precio.count(".") > 1:
        print("Por favor ingrese un número decimal válido.")
        continue

    # Se valida que sea un dígito quitando el punto de decimal para la validación
    if precio.replace(".", "", 1).isdigit():
        # Se convierte el input de precio a float
        precio = float(precio)
        break
    else:
        print("Por favor ingrese un número decimal válido.")

# Validación de cantidad como int
while True:
    # Se solicita la cantidad
    cantidad = input("Ingrese la cantidad: ")

    # Se valida que la cantidad sea un dígito
    if cantidad.isdigit():
        cantidad = int(cantidad)
        break
    else:
        print("Por favor ingrese un número válido.")

# Este es el total del precio
costo_total = precio * cantidad

# Imprime el producto, precio unitario, cantidad, precio total
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


# Este programa es un inventario que solicita al usuario el nombre de un producto, el precio y la cantidad, después multiplica el precio por la cantidad e imprime todos estos datos.