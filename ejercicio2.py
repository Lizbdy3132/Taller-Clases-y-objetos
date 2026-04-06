class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Las dimensiones deben ser mayores a cero")

    def calcular_area(self):
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)

    def obtener_dimensiones(self):
        return self.__largo, self.__ancho