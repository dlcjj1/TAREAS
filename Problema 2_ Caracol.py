# Un caracol cae un pozo de H metros de profundidad. Este caracol durante el día asciende una distancia
# Ld metros, pero durante la noche, al quedarse dormido, resbala y asciende Ln metros. Diseñe un programa
# que simulando el movimiento del caracol para H, Ld y Ln dados por el usuario. El programa debe arrojar
# como resultado en cuantos días el caracol sale del pozo (si es que esto sucede).

# Pedir al usuario los valores de profundidad, ascenso_dia y ascenso_noche
profundidad_del_pozo = float(input("Ingrese la profundidad del pozo en metros: "))
ascenso_en_el_dia = float(input("Ingrese la distancia que asciende el caracol durante el día en metros: "))
ascenso_en_la_noche = float(input("Ingrese la distancia que asciende el caracol durante la noche en metros: "))

# Verificar que los valores sean válidos
if profundidad_del_pozo <= 0 or ascenso_en_el_dia <= 0 or ascenso_en_la_noche < 0:
    print("Los valores deben ser positivos y mayores a cero.")
elif ascenso_en_el_dia <= ascenso_en_la_noche:
    print("El caracol nunca saldrá del pozo.")
else:
    # Inicializar la posición del caracol y el contador de días
    posicion_del_caracol = 0
    dias_en_que_sale = 0

    # Repetir el ciclo mientras el caracol no haya salido del pozo
    while posicion_del_caracol < profundidad_del_pozo:
        # Sumar la distancia que asciende durante el día
        posicion_del_caracol += ascenso_en_el_dia
        # Aumentar el contador de días
        dias_en_que_sale += 1
        # Verificar si el caracol ha salido del pozo
        if posicion_del_caracol >= profundidad_del_pozo:
            break
        # Restar la distancia que asciende durante la noche
        posicion_del_caracol -= ascenso_en_la_noche

    # Mostrar el resultado
    print(f"El caracol sale del pozo en {dias_en_que_sale} días.")