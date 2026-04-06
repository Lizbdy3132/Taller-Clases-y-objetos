class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100")

    def calcular_promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad