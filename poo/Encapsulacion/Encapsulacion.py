"""
Encapsulación
En la mayoría de lenguajes que usan el paradigma de
la POO nos encontramos con el concepto de
encapsulación.

Este consiste en poder ocultar los atributos o métodos de una clase
para que no se puedan cambiar salvo mediante otros métodos que
dispongamos nosotros.

Es decir, la encapsulación consiste en denegar el acceso a los atributos y
métodos internos de la clase desde el exterior.

Supongamos que tenemos una clase Coche con un atributo que sea
color = “negro”.

Cualquiera podría cambiar ese atributo simplemente poniendo
color = “rojo”, por ejemplo. A

Aveces no nos interesa que un atributo se pueda cambiar.
Una forma de “blindarlo” para que no se pueda cambiar su valor es mediante
la encapsulación.

Tendremos la posibilidad de especificar unos modificadores a nuestros
atributos que permitirán o no que su valor se pueda cambiar.


Como norma general tendremos tres modificadores de acceso:

• Public: Los atributos public serán accesibles y modificables desde cualquier
parte de nuestro código.
Es el valor por defecto y sería el equivalente a no poner nada.

• Protected: Podemos acceder a él desde la misma clase y clases hijas.
# HERENCIA O MISMA CLASE

• Private: Accesible únicamente desde su clase.
# SU CLASE

Pero todo esto que hemos explicado no se aplica a Python.
En Python no se especifican métodos o atributos privados ni públicos.
Esto es así porque en Python todos los atributos de una clase son públicos.

Es decir, técnicamente en Python no existe la encapsulación.


No obstante, si queremos tener algún atributo o método “oculto” a la interfaz
pública, es posible indicarlo con la siguiente convención:

1. Por defecto, todos los atributos son públicos.

Python asume que “Aquí todos somos adultos” y sabemos leer la documentación
de nuestro código y utilizarlo bien.

2. Si queremos indicar que algún atributo miembro de una clase es privado,
lo haremos añadiendo el símbolo ‘_’ delante del nombre del tributo.

Por ejemplo:

‘MiClase._atributoPrivado’.
Esto no hace que el atributo sea privado como en otros lenguajes de
programación, es sólo una indicación al programador, para que sepa que debe
usarlo (aunque si quiere, puede hacerlo).

3. Si queremos una “protección extra” utilizaremos 2 guiones ‘__’, en lugar
de uno: p. ej.
‘MiClase.__otroAtribPrivado’.

Esto además hará que el intérprete no lo muestre cuando llamemos a la función
help para obtener más información de la clase, etc.

Por lo tanto, Python proporciona una implementación
conceptual de modificadores de acceso público,
protegido y privado, pero no como otros lenguajes
como C# , Java, C++, etc, es simplemente una
encapsulación “simulada”.


Para acceder a esos datos encapsulados se deberían
crear métodos públicos que hagan de interfaz. En
otros lenguajes les llamaríamos getters y setters y
es lo que da lugar a las propiedades, que no son más
que atributos protegidos con interfaces de acceso:
"""

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")
    def atributo_publico(self):
        return self.__atributo_privado
    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()

#Soy un atributo inalcanzable desde fuera.
#Soy un método inalcanzable desde fuera.

"""
Pero esta simulación de getter y setters es
simplemente eso, una simulación
"""