"""
En la programación orientada a objetos (POO),
una clase abstracta es un concepto fundamental que actúa como un modelo o plantilla para
otras clases.
No está pensada para ser instanciada directamente
 (es decir, no puedes crear objetos directamente de una clase abstracta),
 sino para ser heredada por otras clases, llamadas clases concretas.


otra clase debe heredar la clase abstracta


El propósito principal de una clase abstracta es definir una interfaz común y obligatoria
 para un conjunto de clases relacionadas, garantizando que todas ellas implementen ciertos
 métodos y comportamientos.


la clase que hereda la clase abstracta debe de implementar metodos


Conceptos Clave de las Clases Abstractas en Python
Imposibilidad de Instanciación Directa:
 No puedes crear un objeto directamente de una clase abstracta.
 Si lo intentas, Python lanzará un TypeError.
 Piensa en ella como un concepto o una idea, no como un objeto tangible.

Métodos Abstractos:
Este es el corazón de una clase abstracta.
Un método abstracto es un método declarado en la clase abstracta pero que no tiene una
implementación (cuerpo) en esa clase.
Es como un "contrato" o una "promesa":
la clase abstracta dice "cualquier clase que herede de mí debe implementar este método".

Los métodos abstractos se definen usando el decorador @abstractmethod del módulo abc.

Si una clase concreta (no abstracta) hereda de una clase abstracta y no implementa todos
sus métodos abstractos, tampoco podrá ser instanciada y Python lanzará un TypeError.

las clases que heredan las clases abstractas deben implementar los metodos sin cuerpo
abstractos que tienen las clases abstractas sino no pueden instanciar


Métodos Concretos (Opcional):
 Una clase abstracta puede tener también métodos concretos (con implementación) y atributos.
  Estos métodos y atributos son compartidos por todas las subclases, promoviendo
  la reutilización de código y evitando la duplicación.


las clases bastractas tienen metodos abstractos pero tambien metodos no abstractos



Módulo abc (Abstract Base Classes):
En Python, las clases abstractas se implementan utilizando el módulo incorporado abc.
 Necesitarás importar:
ABC: Una clase auxiliar que sirve como clase base para tus clases abstractas.
Heredar de ABC es la forma más común y sencilla de declarar una clase como abstracta.

abstractmethod: Un decorador que se usa para marcar métodos como abstractos.


¿Por Qué Usar Clases Abstractas? (Ventajas)
Forzar la Implementación de Métodos (Contrato):
Es la razón principal.
Garantiza que cualquier subclase concreta que herede de ella implemente ciertos
métodos esenciales, asegurando una funcionalidad mínima y consistente.
Esto es crucial en equipos grandes o proyectos complejos.

Definir una Interfaz Común:
Proporcionan un marco o esqueleto común para las subclases.
Esto ayuda a mantener la uniformidad en el diseño y comportamiento de las clases
relacionadas.

Reducción de Errores:
Al forzar la implementación, se detectan errores de diseño o implementación en tiempo
de desarrollo (o al intentar instanciar) en lugar de en tiempo de ejecución de una
forma más sutil.

Fomentar la Reutilización de Código:
Los métodos concretos definidos en la clase abstracta pueden ser heredados y utilizados
 por todas las subclases, evitando la duplicación de código
 (Principio DRY - Don't Repeat Yourself).

Polimorfismo:
Las clases abstractas son fundamentales para el polimorfismo.
Puedes escribir código que opere sobre la clase abstracta, y ese
código funcionará automáticamente con cualquier subclase concreta que la implemente,
sin importar cuál sea su tipo específico. Esto hace el código más flexible y extensible.

Ejemplo Práctico: Vehículos
Imagina que estás modelando diferentes tipos de vehículos.
Todos los vehículos tienen algunas características y comportamientos comunes
 (encender, apagar), pero también tienen formas muy diferentes de "moverse".

Python
"""


#Módulo abc (Abstract Base Classes):  En Python, las clases abstractas se implementan
# utilizando el módulo incorporado abc.

#ABC: Una clase auxiliar que sirve como clase base para tus clases abstractas.
#Heredar de ABC es la forma más común y sencilla de declarar una clase como abstracta.

#abstractmethod  decorador para metodos abstractos
from abc import ABC, abstractmethod

# Definimos nuestra clase abstracta Vehiculo que hereda de ABC clase auxiliar base
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método abstracto: Todas las subclases DEBEN implementar cómo se mueven
    @abstractmethod
    def moverse(self):
        pass # No hay implementación aquí, es un contrato

    # Método concreto: Comportamiento compartido que no necesita ser implementado por subclases
    def encender(self):
        print(f"{self.marca} {self.modelo} se ha encendido.")

    # Método concreto: Otro comportamiento compartido
    def apagar(self):
        print(f"{self.marca} {self.modelo} se ha apagado.")

# --- Clases Concretas que heredan de Vehiculo ---

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Implementación OBLIGATORIA del método abstracto moverse()
    def moverse(self):
        print(f"El coche {self.marca} {self.modelo} se desplaza por carretera.")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_montana):
        super().__init__(marca, modelo)
        self.tipo_montana = tipo_montana

    # Implementación OBLIGATORIA del método abstracto moverse()
    def moverse(self):
        print(f"La bicicleta {self.marca} {self.modelo} se mueve pedaleando.")

class Avion(Vehiculo):
    def __init__(self, marca, modelo, altitud_maxima):
        super().__init__(marca, modelo)
        self.altitud_maxima = altitud_maxima

    # Implementación OBLIGATORIA del método abstracto moverse()
    def moverse(self):
        print(f"El avión {self.marca} {self.modelo} está volando por el cielo a {self.altitud_maxima} metros.")


# --- Demostración del uso ---

# Intento de instanciar la clase abstracta (esto generará un TypeError)
try:
    mi_vehiculo_generico = Vehiculo("Genérico", "Concepto")
    print(mi_vehiculo_generico)
except TypeError as e:
    print(f"\n¡Error esperado! No se puede instanciar una clase abstracta directamente: {e}")



print("\n--- Instanciando Clases Concretas ---")
coche = Coche("Toyota", "Corolla", 4)
bicicleta = Bicicleta("Specialized", "Epic", True)
avion = Avion("Boeing", "747", 12000)

coche.encender()
coche.moverse()
coche.apagar()

print("-" * 20)

bicicleta.moverse() # Las bicicletas no se "encienden" en el sentido de un motor, pero heredan el método
                    # Si 'encender' no tuviera sentido, podríamos no ponerlo en Vehiculo o anularlo en Bicicleta
bicicleta.apagar() # Lo mismo para apagar

print("-" * 20)

avion.encender()
avion.moverse()
avion.apagar()

print("-" * 20)

# Polimorfismo: Una función que trabaja con cualquier Vehiculo
def realizar_viaje(vehiculo: Vehiculo):
    print(f"\nPreparando el viaje con {vehiculo.marca} {vehiculo.modelo}...")
    vehiculo.encender()
    vehiculo.moverse()
    vehiculo.apagar()
    print("Viaje completado.")

realizar_viaje(coche)
realizar_viaje(bicicleta)
realizar_viaje(avion)

"""
Detalles del Ejemplo
Vehiculo(ABC): Hereda de ABC para indicar que es una Clase Base Abstracta.

@abstractmethod def moverse(self): pass: Declara moverse como un método abstracto. pass significa que no hay implementación en esta clase. Cualquier clase que herede de Vehiculo debe proporcionar su propia versión de moverse().

Métodos Concretos (encender, apagar): Tienen una implementación completa en Vehiculo. Las subclases (Coche, Bicicleta, Avion) heredan estos métodos y pueden usarlos directamente sin reimplementarlos, lo que ahorra código.

Subclases (Coche, Bicicleta, Avion):

Heredan de Vehiculo.

Obligatoriamente implementan moverse() cada una a su manera, adaptada al tipo de vehículo. Si olvidaras implementar moverse() en, por ejemplo, Coche, Python te daría un TypeError al intentar crear un objeto Coche.

Pueden usar los métodos encender() y apagar() heredados de Vehiculo.

Demostración:

Se muestra cómo intentar instanciar Vehiculo directamente produce un error.

Se crean instancias de las clases concretas (Coche, Bicicleta, Avion) y se utilizan sus métodos.

La función realizar_viaje demuestra el polimorfismo: puede aceptar cualquier objeto que sea una subclase de Vehiculo y llamar a sus métodos encender(), moverse() y apagar() de manera genérica. Cada objeto concreto (coche, bicicleta, avion) ejecutará su propia implementación de moverse().

En resumen, las clases abstractas en Python te permiten diseñar jerarquías de clases robustas y coherentes, aplicando un "contrato" de comportamiento que las subclases deben respetar, mientras que también permiten compartir funcionalidades comunes.
"""