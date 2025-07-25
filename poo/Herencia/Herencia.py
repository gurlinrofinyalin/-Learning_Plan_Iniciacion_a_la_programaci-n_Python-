class Vehiculo():
    #constructor   2 atributos obligatorios  3 por defecto
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

    # metodos
    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print("Marca:", self.marca, "\n","Modelo:", self.modelo,
              "\n","Color:", self.color, "\n","Está arrancado:",
              self.arrancado,"\n","Está parado:", self.parado
              )

class Moto(Vehiculo):
    pass


miCoche = Vehiculo("Renault", "Megane")
miCoche.resumen()
"""
Marca: Renault 
 Modelo: Megane 
 Color: Negro 
 Está arrancado: False 
 Está parado: True
"""
miCoche.arrancar()
miCoche.resumen()
"""
Marca: Renault 
 Modelo: Megane 
 Color: Negro 
 Está arrancado: True 
 Está parado: False
 """

miMoto = Moto("Kawasaki", "Ninja")
miMoto.resumen()
"""
Marca: Kawasaki 
 Modelo: Ninja 
 Color: Negro 
 Está arrancado: False 
 Está parado: True

"""