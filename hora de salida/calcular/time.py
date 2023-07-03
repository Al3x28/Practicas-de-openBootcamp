import datetime

def comprobarhora():
    hora = datetime.datetime.now()

    horaf = hora.strftime('%H')

    

    if int(horaf) >= 19:
        return "son las "+ str(horaf) + " es hora de regresar a casa"
    else:
        restante = 19 - int(horaf) 
        return "son las "+ str(horaf) + " horas todavia te quedan "+ str(restante) +" horas para regresar a casa"

