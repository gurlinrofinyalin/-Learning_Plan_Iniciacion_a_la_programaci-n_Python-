class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
        #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        # AQUI USAMOS EL NOMBRE DE LA CLASE Padre en vez de Super
        Padre.__init__(self, ojos, cejas)
        #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        """
        Utilizando super(). De esta forma es casi el mismo
            código, pero no necesitamos especificar la clase
            padre, por lo que podremos cambiarle el nombre en
            cualquier momento y nuestro código seguirá
            funcional.
        """




Tomas = Hijo('Marrones', 'Negras','Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)