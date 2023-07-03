from pickle import *

class carro:
    def __init__(self, modelo, color, ruedas, puertas):
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self):
        return "El "+ self.modelo + " es de color "+ self.color + " contiene " + self.ruedas + " ruedas y " + self.puertas + " puertas "




coche = carro("VW","Azul","4","2")
print(coche)


archivo = open('detalles_del_vehiculo', 'w+b')

dump(coche,archivo)

archivo.seek(0)
info = load(archivo)

print(info)

archivo.close