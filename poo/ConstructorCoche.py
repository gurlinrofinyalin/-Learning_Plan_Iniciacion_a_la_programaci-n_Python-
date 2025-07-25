# Creación de la clase Coche
class Coche():

    # # Declaración del constructor de la clase Coche
    # def __init__(self):
    #     self.largo = 250
    #     self.ancho = 120
    #     self.ruedas = 4
    #     self.peso = 900
    #     self.color = "rojo"
    #     self.is_enMarcha = False

    # CONSTRUCTOR OFICIAL
    def __init__(self, largo=250, ancho=120, ruedas=4,
                 peso=900, color="rojo", is_enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha

    # variante de constructor
    # @classmethod
    # def por_defecto(cls):
    #     return cls(250, 120, 4, 900, "rojo", False)



    #   Método auxiliar → @classmethod   como CONSTRUCTOR
    """
    cls es la propia clase (a secas, sin instanciar).
Dentro de un @classmethod se usa en lugar de self para:
Poder crear y devolver nuevas instancias de la clase sin necesidad de ya tener una instancia previa.
Mantener el código genérico: si sub-clasificas, cls apuntará a la clase hija sin cambiar nada.
    """
    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)
    """
cls es la clase misma (por ejemplo, Coche si el método está en la clase Coche).
*tupla desempaqueta los elementos de la tupla y los pasa como argumentos posicionales al constructor __init__.
return Coche(tupla[0], tupla[1], tupla[2], ...)
return ... devuelve la nueva instancia ya creada e inicializada.
    """


    # imprimir el objeto sobreescribir el str
    def __str__(self):
        return f"""{self.largo}  {self.ancho} {self.ruedas} {self.peso} {self.color } {self.is_enMarcha }"""
    # destructor
    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")


    # Declaración de métodos
    def arrancar(self): #self hace referencia a la instancia de clase.
        self.is_enMarcha = True #Es como si pusiésemos miCoche.is_enMarcha = True
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()
# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de" , coche_1.largo, "cm.")
coche_1.arrancar()
print(coche_1.estado())
# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:" , coche_1.arrancar())


coche_2 = Coche(420, 150, 4, 1500, "verde",False)

coche_3 = Coche.desde_tupla((300, 150, 4, 1200, "azul", True))
print(coche_1)
print(coche_2)
print(coche_3)
del coche_1
del coche_2
del coche_3

"""
Constructor oficial → __init__
Método auxiliar → @classmethod


Decorador	Primer parámetro	Se refiere a
@staticmethod	—	               nada
@classmethod	cls	             la clase (no la instancia)
método normal	self	        la instancia
"""