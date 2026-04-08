class vehiculo():
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    def infovehiculo (self):
        return f"El vehiculo es de la marca {self.marca} y es del año {self.año}"
 
class coche(vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)          
        self.modelo = modelo
    def infocoche (self):
        return f"El coche es un modelo de referencia {self.modelo}"
    
coche1 = coche("Nissan", 2021, "Exclusive") 
print(coche1.infovehiculo() + ", " + coche1.infocoche())

