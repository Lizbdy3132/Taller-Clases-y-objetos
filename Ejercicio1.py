
class Libro:

    def __init__(self, titulo, autor, numero_de_paginas):
       
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        
    def mostrar_informacion(self):
        print("-----------------------------")
        print("Información del Libro:")
        print("Título: " + self.titulo)
        print("Autor: " + self.autor)
        print("Número de páginas: " + str(self.numero_de_paginas))
        print("-----------------------------")

    def actualizar_paginas(self, nuevas_paginas):
        self.numero_de_paginas = nuevas_paginas
        print("¡El número de páginas ha sido actualizado!")

mi_libro_favorito = Libro("Cien Años de Soledad", "Gabriel García Márquez", 400)

mi_libro_favorito.mostrar_informacion()

mi_libro_favorito.actualizar_paginas(471)

mi_libro_favorito.mostrar_informacion()
