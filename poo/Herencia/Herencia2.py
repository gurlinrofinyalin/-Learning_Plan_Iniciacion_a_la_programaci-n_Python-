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


# hereda el metodo resumen y arrancar y parar
# sobrescribe el metodo resumen , que es metodo padre
# Moto hereda de Vehiculo
# posee un medodo propio que es poner_carenado
class Moto(Vehiculo):
    is_carenado = False

    # Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True

    # La clase Moto sobrescribe el método resumen() heredado del padre

    def resumen(self):
        print("El modelo es una moto","\n", "Marca:", self.marca, "\n","Modelo:", self.modelo, "\n",
              "Color:", self.color, "\n","Está arrancado:", self.arrancado, "\n",
              "Está parado:", self.parado, "\n", "Tiene carenado:", self.is_carenado)


# hereda el metodo resumen del abuelo
# hereda el metodo cponer_carenado de su padre
# esta clase kwad hereda de Moto
# Moto hereda de Vehiculo
class kwad(Moto):
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
El modelo es una moto 
 Marca: Kawasaki 
 Modelo: Ninja 
 Color: Negro 
 Está arrancado: False 
 Está parado: True 
 Tiene carenado: False
"""

miKwad = kwad("Linhai", "LH 500")
miKwad.resumen()
"""
El modelo es una moto 
 Marca: Linhai 
 Modelo: LH 500 
 Color: Negro 
 Está arrancado: False 
 Está parado: True 
 Tiene carenado: False      
"""


"""  SOBREESCRITURA DE METODOS
Como podemos ver en este ejemplo, la clase Moto, a
pesar de haber heredado el método resumen() lo ha
reescrito con nuevas características. Es lo que se
denomina sobreescritura de métodos. Es decir, que
una clase hija herede un método de una clase padre
no significa que esté obligada a usarlo siempre tal
cual lo heredó, lo puede modificar según sus
necesidades. Si no lo modifica, lo heredará tal cual
está implementado en el padre, como es el caso de la
clase Kwad, que ha heredado el método resumen()
de la clase Moto tal y como está implementado, sin
modificarlo.
"""