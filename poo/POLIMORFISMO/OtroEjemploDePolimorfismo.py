class Poligono:
    """
    Clase base para representar un polígono genérico.
    Define el número de lados y el color.
    """
    def __init__(self, num_lados, color=None):
        self.num_lados = num_lados
        self.color = color if color is not None else "sin color" # Valor por defecto más explícito

    def show(self):
        """Muestra las propiedades generales del polígono."""
        print('Polígono:')
        print('Número de lados:', self.num_lados)
        print('Color:', self.color)


class Cuadrado(Poligono):
    """
    Clase que representa un cuadrado, heredando de Poligono.
    Tiene 4 lados y un lado específico.
    """
    def __init__(self, lado, color=None):
        # Llama al constructor de la clase base Poligono
        # Un cuadrado siempre tiene 4 lados.
        Poligono.__init__(self, 4, color)
        self.lado = lado
    # Sobreescribe el método show()
    def show(self):
        """
        Sobreescribe el método show para incluir detalles específicos del cuadrado.
        Llama al show del padre y añade la información del lado.
        """
        super().show() # Llama a Poligono.show()
        print('Lado:', self.lado)


class Triangulo(Poligono):
    """
    Clase que representa un triángulo, heredando de Poligono.
    Tiene 3 lados y una base y altura específicas.
    """
    def __init__(self, base, altura, color=None):
        # Llama al constructor de la clase base Poligono
        # Un triángulo siempre tiene 3 lados.
        Poligono.__init__(self, 3, color)
        self.base = base
        self.altura = altura

    # Sobreescribe el método show()
    def show(self):
        """
        Sobreescribe el método show para incluir detalles específicos del triángulo.
        Llama al show del padre y añade la información de base y altura.
        """
        super().show() # Llama a Poligono.show()
        print('Base:', self.base)
        print('Altura:', self.altura)


# --- Creación de instancias ---
"""
SE SOBREESCRIBEN LOS METODOS SHOY donde 
uno da base  altura como el Triangulo 
y el otro solo da el  lado
"""



# Dos instancias de Triangulo para t1 y t2
t1 = Triangulo(base=5, altura=10, color='azul')
t2 = Triangulo(base=3, altura=6, color='rojo')

# Una instancia de Cuadrado para c1 (ya la tenías)
c1 = Cuadrado(lado=2, color='verde')


# --- Demostración de Polimorfismo ---

# Tupla con dos Triangulos y un Cuadrado
poligonos = (t1, t2, c1)

print("--- Mostrando Polígonos ---")
for poligono in poligonos:
    # La misma llamada 'poligono.show()' se comporta de forma diferente
    # dependiendo del tipo de objeto (Triangulo o Cuadrado).
    poligono.show()
    print("-" * 20) # Separador para mejor legibilidad


"""

Polígono:
Número de lados: 3
Color: azul
Base: 5
Altura: 10
--------------------
Polígono:
Número de lados: 3
Color: rojo
Base: 3
Altura: 6
--------------------
Polígono:
Número de lados: 4
Color: verde
Lado: 2
--------------------


En este ejemplo estamos, primero definiendo la clase
Cuadrado, que hereda de Poligono. Creamos una
tupla con dos Triangulo y un Cuadrado y
recorriéndola con un bucle for. Como vemos,
llamamos al método show de cada elemento de la
tupla. Como es lógico, cada llamada produce el
resultado específico para el tipo de polígono al que
pertenece. Notad que esto en Python es trivial ya
que siempre tratamos directamente con referencias
a objetos, así que la llamada a show es siempre la
correspondiente a la del objeto referenciado.
"""