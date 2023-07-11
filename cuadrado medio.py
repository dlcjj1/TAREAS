print("Ingrese por favor un numero:")
intentos= 0
limite_de_intentos=3

while intentos < limite_de_intentos:
    Valor_del_numero= int(input())
    if len(str(Valor_del_numero))<4:
        print("El numero tiene que ser mayor ó igual a 4 digitos")
        intentos+=1

    else:
        
        for i in range(3):
            Valor_del_numero= str(Valor_del_numero * Valor_del_numero)
            Valor_del_numero= int(Valor_del_numero[2:6])
            print(f"{i+1}. {Valor_del_numero/10000}")
            
    if intentos== limite_de_intentos: 
        print ("Haz excedido el numero de intentos")
    
    



