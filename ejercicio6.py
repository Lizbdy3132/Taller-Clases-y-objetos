class Empleado:
    __total_empleados = 0

    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
        Empleado.__total_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        return cls.__total_empleados

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario(self):
        return self.__salario