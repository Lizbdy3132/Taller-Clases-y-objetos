class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a cero")

    def obtener_precio(self):
        return self.__precio

    def obtener_nombre(self):
        return self.__nombre

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.__precio -= self.__precio * (porcentaje / 100)
        else:
            raise ValueError("El porcentaje debe estar entre 0 y 100")