
class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        nota_minima = 60
        
        if self.calificacion >= nota_minima:
            print("El estudiante " + self.nombre + " ha APROBADO.")
        else:
            print("El estudiante " + self.nombre + " ha REPROBADO.")


estudiante1 = Estudiante("Sofia", 20, 90)
estudiante1.verificar_aprobacion()

estudiante2 = Estudiante("Mateo", 22, 45)
estudiante2.verificar_aprobacion()