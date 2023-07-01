
texto = str(input("ingrse una cadena de texto:"))
print( texto)
def invertir(texto):
    acumulador=""
    for i in range( len (texto)):
        acumulador= texto[i]+ acumulador
    print(acumulador)
invertir(texto)



Invertido= invertir(texto)
texto= texto
if texto == Invertido:
    print (" Los textos son capicúa")
else:
    print (" Los textos no son capicúa")

