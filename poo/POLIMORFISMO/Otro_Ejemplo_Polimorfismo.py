class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    # se llaman depsues de mostrar_detalles
    def __str__(self):
        return f'Empleado: [Nombre:{self.nombre}, Sueldo: {self.sueldo}]'

    #  funcion que se llama
    def mostrar_detalles(self):
        return self.__str__()

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    # se llaman depsues de mostrar_detalles
    # ADEMAS AQUI LLAMAMOS CON SUPER A  str directamente DE EMPLEADO
    # clase de la que hereda , no llama a mostrar_detalles de EMPLEADO
    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'

    #  funcion que se llama
    def mostrar_detalles(self):
        return self.__str__()

# FUNCION INDEPENDIENTE , donde se le pasa el objeto
def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000,'Sistemas')
imprimir_detalles(gerente)

"""
CADA OBJETO tiene su mostrar detalles 
Gerente sobreescribe  el metodo de Empleado 
dando un resultado diferente


mostrar_detalles  llama a str del propio objeto
son distintos 

"""