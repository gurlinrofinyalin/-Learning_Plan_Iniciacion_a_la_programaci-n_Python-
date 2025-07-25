"""
Herencia múltiple
Como hemos comentado anteriormente, Python
admite la herencia múltiple, es decir, admite que una
clase herede de dos o más clases. O dicho de otro
modo, que una clase “hija” pueda heredar de dos o
más clases “padre”. No todos los lenguajes de
programación orientada a objetos soportan esta
característica.
La sintaxis a usar en este caso es simplemente poner
entre paréntesis y separados por una coma las clases
padre de las que heredará nuestra clase hija.

En el siguiente ejemplo la clase bicicleta eléctrica
hereda de vehículos y de vehículos eléctricos:


Simplemente poniendo entre paréntesis las clases de
las que hereda, nuestra clase hija ya tiene todos los
métodos y las propiedades de ambas clases.
Muy importante: Se da preferencia siempre a la
primera clase que se indique entre paréntesis.


PRIORIDAD AL LA PRIMERA CLASE PADRE
EN CONSTRUCTORES
Y EN METODOS


Hereda el constructor de la primera clase que
pusimos en el paréntesis, y en caso de que haya
métodos comunes, también hereda el del primero.



De todas estas opciones debemos quedarnos con el
uso de super() como forma de programar más
correcta.
Nota: En el caso de la Herencia Múltiple super() no
nos sirve. Debemos llamar a los constructores de
ambas clases especificándolas por su nombre y si
cambiamos el nombre u orden de la clase deberemos
especificarlo.


NOS REFEREMOS SI TENEMOS CONSTRUCTORES
"""
class Vehiculos:

    def __init__(self, ruedas= 5, color ="blanco"):
        self.ruedas = ruedas
        self.color = color

    def descripcion(self):
        print("Ruedas: ", self.ruedas, "Color: ", self.color)


class V_electricos:


    def __init__(self, bateria= 30000, voltaje= 24):
        self.bateria = bateria
        self.voltaje = voltaje

    def descripcion(self):

        print("Bateria: ", self.bateria,", Voltaje: ", self.voltaje)

# esta clase hereda de dos clases padre
class B_electrica(Vehiculos, V_electricos):

    def __init__(self, ruedas= 5, color ="blanco", bateria= 30000, voltaje= 24):  # creamos el constructor de la clase especificando atributos
        # AQUI USAMOS EL NOMBRE DE LA CLASE Padre en vez de Super
        Vehiculos.__init__(self,ruedas, color)
        V_electricos.__init__(self, bateria, voltaje)

    def descripcion(self):
        Vehiculos.descripcion(self)  # aqui llama al metodo de clase padre
        V_electricos.descripcion(self)


es = B_electrica()

es.descripcion()



print(" \nDIVISION DE PROGRAMAS\n ")


"""
Para sobrescribir un método heredado de la clase
padre, simplemente volvemos a escribir el método
con todos sus argumentos y añadimos el nuevo
argumento.
Por ejemplo, suponiendo que tenemos un método
estado() de la clase padre “vehículo”:
"""
class Vehiculo:
    modelo = "Desconocido"
    marca = "Desconocida"

    def __init__(self, modelo, marca):
        self.marca = marca
        self.modelo  = modelo

    def estado(self):
        print("Marca", self.marca, "Modelo",
              self.modelo)

class Coche(Vehiculo):
    cilindrada =6000 ## aqui  como hago que coja por defecto

    # podemos quitar cilindrada=4000 si queremos instanciar con modelo y marca solo
    # cogera el atriuto arriba
    def __init__(self, modelo, marca, cilindrada=4000):
        super().__init__(modelo, marca)
        self.cilindrada = cilindrada # si se comenta este coje el atributo 6000

    def setCilindrada(self):
        self.cilindrada = 3000
    # sobreescribir el metodo
    def estado(self):
        print("Marca", self.marca, "Modelo",
              self.modelo, "Cilindrada", self.cilindrada)

ve = Coche("Mondeo","Renault")
#ve.setCilindrada()
ve.estado()



"""
Cómo funciona la jerarquía de atributos en Python
Cuando accedes a un atributo en una instancia (como ve.cilindrada), Python sigue este orden de búsqueda:

Atributos de instancia: Primero busca si el atributo cilindrada ha sido definido directamente en la instancia ve (es decir, si existe un self.cilindrada asignado en el __init__ o en otro método después de que el objeto fue creado).

Atributos de clase: Si no encuentra el atributo en la instancia, lo busca en la clase a la que pertenece la instancia (Coche en tu caso).

Atributos de clases base: Si tampoco lo encuentra en la clase, lo busca en las clases de las que hereda (Vehiculo en tu caso), y así sucesivamente.
"""