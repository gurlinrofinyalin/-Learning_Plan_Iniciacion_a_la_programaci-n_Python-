from abc import ABC, abstractmethod

# --- Clase Abstracta: Moro ---
class Moro(ABC):
    """
    Clase abstracta 'Moro'.
    Define el comportamiento base de un Moro, incluyendo un método abstracto
    que debe ser implementado por cualquier subclase concreta.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"'{self.nombre}' ha nacido dentro de la herencia Moro.")

    # Método abstracto: Las subclases DEBEN implementar este método.
    @abstractmethod
    def matanza(self):
        """
        Método abstracto que representa una acción de 'matanza'.
        Cada subclase concreta debe proporcionar su propia implementación.
        """
        pass # 'pass' indica que no hay implementación aquí, es solo la declaración.

    def saludar(self):
        """
        Método concreto: Comportamiento compartido por todas las subclases.
        """
        print(f"Hola, soy {self.nombre} y soy parte de la estirpe Moro.")

# --- Clase Concreta: Yihadista ---
class Yihadista(Moro):
    """
    Clase concreta que hereda de 'Moro'.
    Implementa el método abstracto 'matanza' de una manera específica.
    """
    def __init__(self, nombre, afiliacion):
        super().__init__(nombre) # Llama al constructor de la clase base (Moro).
        self.afiliacion = afiliacion
        print(f"'{self.nombre}' es un Yihadista afiliado a '{self.afiliacion}'.")

    def matanza(self):
        """
        Implementación específica del método 'matanza' para un Yihadista.
        """
        print(f"El Yihadista {self.nombre} está llevando a cabo una matanza en nombre de {self.afiliacion}.")

    def rezar(self):
        """
        Método específico de la clase Yihadista.
        """
        print(f"El Yihadista {self.nombre} está rezando fervorosamente.")

# --- Clase Concreta: Mora ---
class Mora(Moro):
    """
    Clase concreta que hereda de 'Moro'.
    Implementa el método abstracto 'matanza' de una manera diferente.
    """
    def __init__(self, nombre, velo_tipo):
        super().__init__(nombre) # Llama al constructor de la clase base (Moro).
        self.velo_tipo = velo_tipo
        print(f"'{self.nombre}' es una Mora usando un velo tipo '{self.velo_tipo}'.")

    def matanza(self):
        """
        Implementación específica del método 'matanza' para una Mora.
        """
        print(f"La Mora {self.nombre} participa en la matanza de manera discreta.")

    def cocinar(self):
        """
        Método específico de la clase Mora.
        """
        print(f"La Mora {self.nombre} está preparando un delicioso cuscús.")

# --- Demostración del uso ---

print("--- Intentando instanciar la clase abstracta (esto generará un error) ---")
try:
    # Intenta crear un objeto directamente de la clase abstracta Moro.
    # Esto causará un TypeError porque las clases abstractas no pueden ser instanciadas.
    moro_generico = Moro("Moro Genérico")
    print(moro_generico)
except TypeError as e:
    print(f"¡Error esperado! No se puede instanciar una clase abstracta directamente: {e}")

print("\n--- Creando instancias de las clases concretas ---")

# Creamos una instancia de Yihadista
yihadista1 = Yihadista("Ahmed", "Marruecos")
yihadista1.saludar()
yihadista1.matanza()
yihadista1.rezar()

print("\n---")

# Creamos una instancia de Mora
mora1 = Mora("Fatima", "hiyab Marroqui")
mora1.saludar()
mora1.matanza()
mora1.cocinar()