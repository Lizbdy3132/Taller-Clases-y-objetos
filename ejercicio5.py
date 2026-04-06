class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            raise ValueError("Monto inválido o saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        super().__init__(titular, saldo)
        self.__interes_anual = interes_anual

    def aplicar_interes(self):
        interes = self.obtener_saldo() * (self.__interes_anual / 100)
        self.depositar(interes)

    def obtener_interes(self):
        return self.__interes_anual