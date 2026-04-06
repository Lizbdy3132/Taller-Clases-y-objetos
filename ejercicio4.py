class Libro:
    def __init__(self, titulo, autor, paginas_totales):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas_totales = paginas_totales
        self.__pagina_actual = 1

    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas <= self.__paginas_totales:
            self.__pagina_actual += paginas
        else:
            raise ValueError("No se puede superar el número total de páginas")

    def retroceder_paginas(self, paginas):
        if self.__pagina_actual - paginas >= 1:
            self.__pagina_actual -= paginas
        else:
            raise ValueError("No se puede retroceder más allá de la página 1")

    def obtener_pagina_actual(self):
        return self.__pagina_actual

    def obtener_informacion(self):
        return f"Libro: {self.__titulo}, Autor: {self.__autor}, Total páginas: {self.__paginas_totales}, Página actual: {self.__pagina_actual}"