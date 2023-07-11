# Diseñe un programa que solicite a un usuario el valor de N para generar números aleatorios con la técnica del cuadrado
# medio, el programa debe verificar que tal número posea al menos 4 dígitos, en caso contrario arroje un mensaje de error
# y vuelva a solicitar el número N. Debe otorgarle al usuario como máximo, 3 oportunidades para introducir el número 
# correctamente.

# Contador de oportunidades
oportunidades = 0

while oportunidades < 3:
    # Solicitar el número semilla al usuario
    numero_semilla = input("Escriba el número semilla: ")
    tamaño_numero_semilla = len(numero_semilla)

    # Verificar que la semilla tenga al menos 4 dígitos
    if tamaño_numero_semilla < 4:
        print("Error: El número semilla debe tener al menos 4 dígitos")
        oportunidades += 1
    else:
        break

# Verificar si se agotaron las oportunidades
if oportunidades == 3:
    print("Se agotaron las oportunidades. Vuelve a ejecutar el programa.")
    exit()

print("Cantidad de dígitos: ", tamaño_numero_semilla)
numero_semilla_1 = int(numero_semilla)

# Calcular el primer dígito del número central
primer_digito_numero_1 = int((len(str(numero_semilla_1**2)) - tamaño_numero_semilla) / 2)

# Bucle para generar números aleatorios
numeros_generados = 0
while numeros_generados < 3:
    cuadrado_numero_1 = numero_semilla_1**2
    cuadrado_numero_1 = str(cuadrado_numero_1)
    numero_central_1 = cuadrado_numero_1[primer_digito_numero_1:primer_digito_numero_1+tamaño_numero_semilla]
    print (" {}. {}".format(numeros_generados + 1,numero_central_1))
    # imprime en la pantalla el número generado en cada iteración del bucle while. La función format() reemplaza las llaves {} en la cadena de 
    # texto con los valores de las variables oportunidades y numero_central_1. Por lo tanto, en cada iteración del bucle, se imprimirá el valor 
    # de la variable oportunidades seguido del número generado en esa iteración.
    numero_semilla_1 = int(numero_central_1)
    numeros_generados += 1