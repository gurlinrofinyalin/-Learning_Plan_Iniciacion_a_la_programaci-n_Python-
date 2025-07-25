"""
Jerarquía de clases sin usar super(), sobrescribiendo
los atributos del padre:

"""
class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
    #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas


class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el  constructor
        # ESTOS SE ESCRIBEN  sin el super
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        # ESTE ES ATRIBUTO DE LA CLASE Hijo
        self.cara = cara #Especificamos el nuevo atributo para Hijo

Tomas = Hijo('Marrones', 'Negras','Larga') #Instanciamos
print(Tomas.ojos, Tomas.cejas, Tomas.cara) #Imprimimos los atributos del objeto