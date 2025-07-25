"""
Polimorfismo
Si hablamos de herencia, tenemos que hablar de
polimorfismo.

Este término se refiere a la capacidad
de que todos los objetos pertenecientes a una misma
familia de clases, es decir que heredan de la misma
clase, pueden ser llamados con los métodos de la
clase padre que han sobrecargado,

pero se
comportarán con las llamadas a sus propios métodos
sobrecargados.

El polimorfismo es una propiedad de la herencia por
la que objetos de distintas subclases pueden
responder a una misma acción.

El polimorfismo está implícito en Python, ya que
todas las clases son subclases de una superclase
común llamada Object.

Por ejemplo, la siguiente función aplica una rebaja al
precio de un producto:

"""

# FUNCON INDEPENDIENTE
# --- Función para aplicar una rebaja (Demostración de Polimorfismo) ---

def rebajar_producto(producto, rebaja_porcentaje):
    """
    Aplica una rebaja porcentual al precio de un producto.
    Gracias al polimorfismo, esta función no necesita saber el tipo exacto de 'producto',
    solo que tiene un atributo 'pvp'.
    """
    if not hasattr(producto, 'pvp'):
        print(f"Error: El objeto {type(producto).__name__} no tiene un atributo 'pvp'.")
        return

    # Convertir rebaja a un decimal para el cálculo
    descuento_valor = producto.pvp * (rebaja_porcentaje / 100)
    producto.pvp -= descuento_valor
    print(f"Rebaja del {rebaja_porcentaje}% aplicada. Nuevo PVP: {producto.pvp:.2f} €")



"""
Bebida padre 
Alimento hija 
Producto hija
ObjetoSinPVP  no hereda de nadie
"""
class Producto:
    """Clase base para representar un producto genérico."""
    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = float(pvp)  # Aseguramos que PVP sea un número flotante
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        """Método para representar el objeto como una cadena de texto."""
        return (f"REFERENCIA: {self.referencia}\n"
                f"NOMBRE: {self.nombre}\n"
                f"PVP: {self.pvp:.2f} €\n"  # Formateamos a 2 decimales
                f"DESCRIPCIÓN: {self.descripcion}\n"
                f"PRODUCTOR: {self.productor}\n"
                f"DISTRIBUIDOR: {self.distribuidor}")




class Alimento(Producto):
    """Clase para productos de tipo alimento."""
    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor, fecha_caducidad="N/A"):
        super().__init__(referencia, nombre, pvp, descripcion, productor, distribuidor)
        self.fecha_caducidad = fecha_caducidad # Atributo específico de Alimento

    def __str__(self):
        """Sobreescribe el método __str__ para incluir la fecha de caducidad."""
        base_str = super().__str__()
        return f"{base_str}\nFECHA CADUCIDAD: {self.fecha_caducidad}"



class Bebida(Producto):
    """Clase para productos de tipo bebida."""
    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor, volumen_ml=None):
        super().__init__(referencia, nombre, pvp, descripcion, productor, distribuidor)
        self.volumen_ml = volumen_ml # Atributo específico de Bebida

    def __str__(self):
        """Sobreescribe el método __str__ para incluir el volumen."""
        base_str = super().__str__()
        return f"{base_str}\nVOLUMEN: {self.volumen_ml} ml" if self.volumen_ml else base_str



class ObjetoSinPVP:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Objeto sin PVP: {self.nombre}"

# --- Prueba de Polimorfismo ---

print("--- Producto de Alimento ----------------------------------------------")
# Usamos los datos de tu imagen
alimento_aceite = Alimento(
    referencia="2035",
    nombre="Botella de Aceite de Oliva",
    pvp=5.0,  # Inicializamos con 5.0
    descripcion="250 ML",
    productor="La Aceitera",
    distribuidor="Distribuciones SA",
    fecha_caducidad="31/12/2025"
)

print("Antes de la rebaja:")
print(alimento_aceite, "\n")

# Aplicamos la rebaja del 10%
rebajar_producto(alimento_aceite, 10)
print("\nDespués de la rebaja:")
print(alimento_aceite)

print("\n" + "="*40 + "\n")

print("--- Producto de Bebida -------------------------------------------------------------")
bebida_agua = Bebida(
    referencia="1001",
    nombre="Agua Mineral",
    pvp=1.50,
    descripcion="Botella de agua",
    productor="Manantial Claro",
    distribuidor="Distribuciones SA",
    volumen_ml=1000
)

print("Antes de la rebaja:")
print(bebida_agua, "\n")

# Aplicamos la rebaja del 5%
rebajar_producto(bebida_agua, 5)
print("\nDespués de la rebaja:")
print(bebida_agua)

print("\n" + "="*40 + "\n")



print("--- Objeto sin PVP (para demostrar el manejo de errores) -----------------------------------------")
objeto_raro = ObjetoSinPVP("Un cacharro")
print(objeto_raro, "\n")
rebajar_producto(objeto_raro, 10)