"""Super()
Esta función nos permite invocar y conservar un
método o atributo de una clase padre (primaria)
desde una clase hija (secundaria) sin tener que
nombrarla explícitamente. Esto nos brinda la ventaja
de poder cambiar el nombre de la clase padre (base)
o hija (secundaria) cuando queramos y aun así
mantener un código funcional, sencillo y mantenible.


Supongamos que queremos que una clase hija o
secundaria herede los atributos de la clase padre. Si
nosotros no recurrimos a la función super(), o
llamamos al constructor init especificando los
atributos, deberemos reescribirlos, lo cual en una
clase por ejemplo con 20 atributos sería una pérdida
de tiempo enorme.
Para personalizar el constructor del padre de acuerdo
a las necesidades del hijo se usa super().
"""


class Persona():
    def __init__(self, nombre, edad, lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    def descripcion(self):
        print("El nombre es ",
        self.nombre, ", tiene ", self.edad, " años", " y es de ", self.lugar)
class Empleado(Persona):
    # constructor
    def __init__(self, salario,antiguedad, nombre_emp, edad_emp,lugar_epm):
        #Persona.__init__(nombre_emp, edad_emp, lugar_epm)
        # se puede usar el nombre de la clase de la que hereda
        # en vez de usar el super()
        super().__init__(nombre_emp, edad_emp, lugar_epm)
        # nombre edad y lugar son llamados por super a la clase padre
        # llamando al contructor
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion() # aqui llama al metodo de clase padre
        # no lo sobreescribe
        print("Salario: ", self.salario,
              ", antiguedad: ", self.antiguedad)

# si haces una instancia de Persona solo necesitas  nombre edad y lugar
Angel = Persona("Angel", 43, "Malaga")
Angel.descripcion()
# si creas una clase Empleado necesitas salario antiguedad  nombre
# edad y lugar
Empleado1 = Empleado(2000, 2017, "Manolo",
                     33, "Madrid")
Empleado1.descripcion()