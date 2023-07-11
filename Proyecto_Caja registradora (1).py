# Crear un diccionario para almacenar los productos y sus precios
catalogo_de_productos = {
  'chocolate': 0.99,
  'bombones': 0.79,
  'caramelos': 0.69,
  'mani': 1.49,
  'danndy': 2.99
}

# Crear un diccionario para almacenar el stock de cada producto
almacen = {
  'chocolate': 20,
  'bombones': 15,
  'caramelos': 25,
  'mani': 10,
  'danndy': 12
}

# Crear una lista vacía para guardar la lista de compras del cliente
lista_de_compras = []

# Crear una variable para guardar el total de la compra
total = 0

# Crear un bucle while para permitir múltiples transacciones
while True:
  # Mostrar un menú con las opciones disponibles tanto para el cliente como para el administrador 
  print("Bienvenido a la tienda de comestibles S. D. C")
  print("Opciones:")
  print("1. Introducir un producto")
  print("2. Comprar un producto")
  print("3. Ver el total de la compra")
  print("4. Salir del programa")
  print("NOTA: la opcion 1 es solo para el administrador del almacen, las demás son para el cliente")

  # Pedir al usuario que elija una opción
  opcion = input("Elige una opción: ")

  # Si el usuario elige la opción 1, introducir un producto
  if opcion == "1":
    # Pedir al usuario que introduzca el nombre, el precio y la cantidad del producto
    nombre_producto = input("Introduce el nombre del producto: ")
    precio_producto = float(input("Introduce el precio del producto: "))
    cantidad_producto = int(input("Introduce la cantidad del producto: "))

    # Añadir el producto y su precio al diccionario de productos
    catalogo_de_productos[nombre_producto] = precio_producto

    # Añadir el producto y su cantidad al diccionario de stock
    almacen[nombre_producto] = cantidad_producto

    # Mostrar un mensaje de confirmación
    print(f"Has introducido el producto {nombre_producto} con un precio de {precio_producto} y una cantidad de {cantidad_producto}")
    # La f en esa línea de comando significa que se trata de una f-string o cadena de texto formateada1. 
    # Las f-strings son una forma de insertar el valor de las expresiones de Python dentro de una cadena de texto, 
    # usando una sintaxis mínima. Por ejemplo, si tienes una variable llamada NOMBRE, puedes mostrarla dentro de 
    # una cadena de texto usando {nombre} entre llaves. La f-string evaluará la expresión entre llaves y la 
    # reemplazará por su valor

  # Si el usuario elige la opción 2, comprar un producto
  elif opcion == "2":
    # Mostrar los productos disponibles y sus precios
    print("Productos disponibles:")
    for producto in catalogo_de_productos:
      print(f"{producto}: {catalogo_de_productos[producto]}")

    # Pedir al usuario que introduzca el nombre y la cantidad del producto que quiere comprar
    nombre_producto = input("Introduce el nombre del producto que quieres comprar: ")
    cantidad_producto = int(input("Introduce la cantidad que quieres comprar: "))

    # Comprobar si el producto existe en el diccionario de productos
    if nombre_producto in catalogo_de_productos:
      # Comprobar si hay suficiente stock del producto
      if cantidad_producto <= almacen[nombre_producto]:
        # Crear un diccionario para guardar los detalles del producto comprado
        compra = {
          'Nombre del producto': nombre_producto,
          'Precio del producto': catalogo_de_productos[nombre_producto],
          'Cantidad del producto': cantidad_producto
        }

        # Añadir el diccionario a la lista de compras
        lista_de_compras.append(compra)

        # Restar la cantidad comprada al stock del producto
        almacen[nombre_producto] -= cantidad_producto

        # Mostrar un mensaje de confirmación
        print(f"Has comprado {cantidad_producto} {nombre_producto} por un total de {cantidad_producto * catalogo_de_productos[nombre_producto]}")

      # Si no hay suficiente stock, mostrar un mensaje de error
      else:
        print(f"Lo sentimos, no tenemos suficiente en el almacen del producto {nombre_producto}")
    
    # Si el producto no existe, mostrar un mensaje de error
    else:
      print(f"Lo sentimos, no tenemos ese producto")

  # Si el usuario elige la opción 3, ver el total de la compra
  elif opcion == "3":
    # Usar un bucle for para recorrer la lista de compras y sumar el total
    for compra in lista_de_compras:
      total += compra['Cantidad del producto'] * compra['Precio del producto']
    
    # Mostrar el total de la compra
    print(f"El total de tu compra es: {total}")

  # Si el usuario elige la opción 4, salir del programa
  elif opcion == "4":
    # Mostrar un mensaje de despedida
    print("Gracias por usar la aplicación. ¡Hasta pronto!")

    # Romper el bucle while
    break

  # Si el usuario elige una opción inválida, mostrar un mensaje de error
  else:
    print("Opción inválida. Por favor, elige una opción válida.")