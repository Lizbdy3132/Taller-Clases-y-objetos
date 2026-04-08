class animal():
    def __init__(self, nombre, especie):
       self.nombre = nombre
       self.especie = especie
    
    def infoanimal(self): 
      return f"se llama {self.nombre} y es su especie es {self.especie}"
  
class perro(animal):
      def __init__(self, nombre, especie, raza):
          super().__init__(nombre, especie)
          self.raza = raza
      def infoperro(self):
              return f"La Mascota se llama {self.nombre} y es un {self.especie} de raza {self.raza}"
          
perro1 = perro("Kira", "perro", "shih tzu")

print(perro1.infoperro())