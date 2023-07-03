class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 4

class coche(Vehiculo):
    velocidad = "20K/H"
    cilindrada = 6


VW = coche()

print("El color del coche es "+VW.color)
print("El coche cuenta con "+ str(VW.ruedas))
print("El coche tiene "+ str(VW.puertas))
print("Tiene una velocidad de "+VW.velocidad)
print("Ademas es de "+str(VW.cilindrada)+" cilindros")