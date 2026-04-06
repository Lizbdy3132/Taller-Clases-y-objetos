class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        suma = 0
        reverso = numero[::-1]
        for i in range(len(reverso)):
            digito = int(reverso[i])
            if i % 2 == 1:
                digito *= 2
                if digito > 9:
                    digito -= 9
            suma += digito
        return suma % 10 == 0

    def obtener_numero(self):
        return self.__numero