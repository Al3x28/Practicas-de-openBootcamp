class Alumno():

    def Constructor  (self, nombre, nota):
        self.nombre=nombre
        self.nota=nota


    def Resultado(self):
        if int(self.nota) >= 5:
            print(self.nombre + " aprobo la materia con: "+ str(self.nota))
            print(" ")
        else:
            print(self.nombre + " reprobo la materia con: "+ str(self.nota))
            print(" ")



estudiante= Alumno()

estudiante2= Alumno()

estudiante3= Alumno()

estudiante4=Alumno()

estudiante.Constructor("Maria", 8)
estudiante2.Constructor("Alejandro", 6)
estudiante3.Constructor("Carlos", 3)
estudiante4.Constructor("Valeria", 5)

estudiante.Resultado()
estudiante2.Resultado()
estudiante3.Resultado()
estudiante4.Resultado()