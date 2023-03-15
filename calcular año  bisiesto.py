def calularaño(año):
    resultado = año/4
 
    if int(resultado) == resultado:
        resultado = año/100
        if int(resultado) == resultado:
            resultado = año/400
            if int(resultado) == resultado:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print("Ingrese el año que desea verificar")
año= int(input())

bisiesto = calularaño(año)

if bisiesto == True:
    print('el año: '+ str(año) +' es bisiesto')
else:
    print('el año: '+ str(año) +' no es bisiesto')