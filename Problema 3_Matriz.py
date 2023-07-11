# Realice un programa que genere una lista de listas, que emule a una matriz de orden NxM, con N y M dados por el usuario.

# Pedir al usuario los valores de N=filas y M=columnas
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear una matriz de tamaño N x M y la llena con ceros
matriz = [[0 for j in range(columnas)] for i in range(filas)]

# Inicializar el contador que llevará el valor de cada elemento de la matriz
contador = 1

# Recorrer la matriz por filas
for i in range(filas):
    # Si la fila es par, recorrer la matriz de izquierda a derecha
    if i % 2 == 0:
        for j in range(columnas):
            # Asignar el valor del contador al elemento actual
            matriz[i][j] = contador
            # Incrementar el contador en uno
            contador += 1
    # Si la fila es impar, recorrer la matriz de derecha a izquierda
    else:
        for j in range(columnas-1, -1, -1):
            # Asignar el valor del contador al elemento actual
            matriz[i][j] = contador
            # Incrementar el contador en uno
            contador += 1

# Imprimir la matriz por pantalla
for fila in matriz:
    print(fila)