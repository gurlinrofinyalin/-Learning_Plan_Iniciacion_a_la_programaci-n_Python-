### No intentes entender este código, sólo fíjate en cómo se utiliza abajo
# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre,apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


# Y otra para las empresas
class Empresa:
    def __init__(self, clientes=[]):
            self.clientes = clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
            return
        print("Cliente no encontrado")


    def borrar_cliente(self, dni=None):
        print(f"{self.clientes}  {type(self.clientes)}")
        # lista de objetos self.clientes
        # [<__main__.Cliente object at 0x7f6957a10ad0>, <__main__.Cliente object at 0x7f6957a10b10>]  <class 'list'>
        for i,c in enumerate(self.clientes):
            print(f" {i}  {c}  {type(c)}")
            #  0  Hector Costa Guzman  <class '__main__.Cliente'>
            #  1  Juan Gonzalez Marquez  <class '__main__.Cliente'>
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras
# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan","Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector,juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)

"""
==LISTADO DE CLIENTES==
[<__main__.Cliente object at 0x7f6957a10ad0>, <__main__.Cliente object at 0x7f6957a10b10>]

==MOSTRAR CLIENTES POR DNI==
Hector Costa Guzman

==BORRAR CLIENTES POR DNI==
[<__main__.Cliente object at 0x7f6957a10ad0>, <__main__.Cliente object at 0x7f6957a10b10>]  <class 'list'>
 0  Hector Costa Guzman  <class '__main__.Cliente'>
 1  Juan Gonzalez Marquez  <class '__main__.Cliente'>
Cliente no encontrado
[<__main__.Cliente object at 0x7f6957a10ad0>, <__main__.Cliente object at 0x7f6957a10b10>]  <class 'list'>
 0  Hector Costa Guzman  <class '__main__.Cliente'>
 1  Juan Gonzalez Marquez  <class '__main__.Cliente'>
Juan Gonzalez Marquez > BORRADO

==LISTADO DE CLIENTES==
[<__main__.Cliente object at 0x7f6957a10ad0>]
"""


"""
==LISTADO DE CLIENTES== [<__main__.Cliente object at 0x0000023F567B42E8>,
<__main__.Cliente object at 0x0000023F567B4320>]
==MOSTRAR CLIENTES POR DNI== 
Hector Costa Guzman
Cliente no encontrado
==BORRAR CLIENTES POR DNI==
Cliente no encontrado Juan Gonzalez Marquez > BORRADO
==LISTADO DE CLIENTES==
[<__main__.Cliente object at 0x0000023F567B42E8>]"""