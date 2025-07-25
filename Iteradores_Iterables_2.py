
#Creando nuestros propios iteradores

"""
Ahora que entendemos completamente cómo
funciona el protocolo de iteración de Python y qué son
los iterables y los iteradores, estamos preparados para
crear nuestros propios objetos iterables e iteradores.

Como hemos visto, un objeto iterador es aquel que
implementa el metodo __next__ especificando cuál
va a ser el siguiente elemento a devolver tras cada
llamada.

 vamos a crear nuestro primer objeto iterador:

"""


### SU CODIGO  PROFESOR  ITERADOR  que tiene tanto iter como next ####
"""
Al haber definido los métodos __iter__ y __next__,
nuestra clase ahora es un iterable y un iterador a la
vez. """
class Repetidor:
    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0

    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item

    """ Para convertirlo en un iterable simplemente hay que 
    implementar el método __iter__:
    
    Este método es esencial para que un objeto sea iterable. 
    Cuando usas un objeto en un bucle for, Python llama a __iter__().
    Para un iterador (como Repetidor en este caso), __iter__() 
    simplemente debe devolver self (la propia instancia del iterador). 
    Esto permite que el iterador se use directamente en un bucle for.
    
    Notad que, como Repetidor ya era un iterador, puede
    devolverse a sí mismo usando la referencia a self.
    
    """
    def __iter__(self):
        # Un iterador siempre debe devolverse a sí mismo en __iter__
        return self


try:
    # Vamos a recorrerlo manualmente:
    rep = Repetidor(3, 'Python', )
    print(next(rep))  # 'Python'
    print(next(rep))  # 'Python'
    print(next(rep))  # 'Python'
    print(next(rep))
except StopIteration:
    print("el numero de veces se ha consumido con 3")

"""
Pero fijaos que aún no puede ser recorrido por un
bucle for porque nuestra clase no es iterable:
"""
try:
    for r in Repetidor(3, 'Python!'):
        print(r, end=' ')
except TypeError:
    print("Repartidor no es un iterable")

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Iteradores_Iterables_2.py", line 163, in <module>
    for r in Repetidor(3, 'Python!'):
TypeError: 'Repetidor' object is not iterable
"""





print("\n MI CODIGO  \n")

# CLASE y ejecucion
# si tiene iter y next es iterador

"""
permite que tu clase Repetidor funcione perfectamente con todas las 
características  de iteración de Python, 
incluidos los bucles for y la función next().
"""
class Repetidor2:
    """
    Un iterador que repite un 'item' un número especificado de 'veces'.
    """

    def __init__(self, veces, item):
        self.veces = veces # Almacena cuántas veces queremos repetir el item.
        self.item = item # Almacena el valor que queremos repetir.

        #Inicializa un contador a 0.
        # Lo usaremos para saber cuántas veces hemos devuelto el item.
        self.counter = 0


    """
    
    
    Este método es esencial para que un objeto sea iterable. 
    Cuando usas un objeto en un bucle for, Python llama a __iter__().
    Para un iterador (como Repetidor en este caso), __iter__() 
    simplemente debe devolver self (la propia instancia del iterador). 
    Esto permite que el iterador se use directamente en un bucle for.
    
    • Iterable: 
    Un objeto iterable es un objeto que devuelve un iterador. 
    Para ello implementa el método __iter__.
    """
    def __iter__(self):
        # Un iterador siempre debe devolverse a sí mismo en __iter__
        return self#aquí devuelve self porque él mismo es un iterador
    # Cuando una clase es su propio iterador, significa que ella misma
    # lleva el control del recorrido (posición actual, etc.).





    """
    Este método es el corazón del iterador. 
    Se llama cada vez que se pide el "siguiente" elemento del iterador 
    (por ejemplo, en cada iteración de un bucle for o cuando llamas a next()).
   
 
    • Iterador: Un iterador es un objeto que implementa:
    __next__() → para dar el siguiente valor.
    pero tambien tienen iter, el de arriba
    __iter__() que devuelve self → para que pueda usarse en bucles for, 
    iter(), etc.
            
    
    if self.counter == self.veces:: 
    Esta es la condición de parada. 
    Si el contador ya alcanzó el número de veces que se debe repetir el item,
     significa que ya no quedan más elementos.
    
    raise StopIteration('Iterador consumido'): 
    Cuando no quedan más elementos, el iterador debe levantar una excepción StopIteration. 
    Es la señal estándar en Python para indicar que la iteración ha terminado.
    
    self.counter += 1: Incrementamos el contador cada vez que devolvemos un item.
    
    return self.item: Devolvemos el item actual.
    """
    def __next__(self):
        if self.counter == self.veces:
            # Cuando el contador llega al número de repeticiones,
            # levantamos StopIteration para indicar que no hay más elementos.
            raise StopIteration('Iterador consumido')

        self.counter += 1
        return self.item





#from repetidor import Repetidor

# Creamos una instancia de Repetidor que repetirá 'Hola' 3 veces
rep = Repetidor2(3, 'Hola')



print("--- Iterando con un bucle for ---")
for elemento in rep:
    print(elemento)
# Salida:
# Hola
# Hola
# Hola




print("\n--- Iterando manualmente con next() ---")
"""
Cuando un iterador (como nuestra clase Repetidor) se queda sin elementos para devolver, 
debe lanzar (o "generar") una excepción StopIteration. 
Y si tú, como programador, estás llamando a next() directamente 
(en lugar de usar un for loop, que lo maneja automáticamente), 
entonces debes "recoger" o "capturar" esa excepción.
"""



# Creamos otra instancia porque el iterador anterior ya fue consumido
rep_manual = Repetidor2(2, 'Manzana')

try:
    print(next(rep_manual)) # O rep_manual.__next__()
    print(next(rep_manual))
    print(next(rep_manual)) # Esto generará StopIteration
except StopIteration as e:
    print(f"Excepción capturada: {e}")




print("\n--- Probando con cero repeticiones ---")
rep_cero = Repetidor2(0, 'Nada')
try:
    print(next(rep_cero))
except StopIteration as e:
    print(f"Excepción capturada: {e}") # Se activará inmediatamente

"""
En este ejemplo estamos creando una clase que
permite ir generando repeticiones del parámetro que
le hayamos pasado al constructor. Con esto hemos
creado nuestro primer iterador.
"""






#  ITERABLE PERO NO ITERADOR
# si tiene iter  pero no tiene  next es iterable
# para ser iterable debo implementar el __iter__
#para ser iterador deberia de implementar el __next__

"""
Tened en cuenta que es posible crear iterables que
no son iteradores: con que devuelvan un objeto
iterador, que no tiene por qué ser uno mismo, ya
basta:
"""
class Repetidor4():

    # Si quieres que tu clase sea un iterable pero no un iterador,
    # debes devolver un iterador de otro objeto iterable,
    def __init__(self, veces, *items):
        self.veces = veces
        self.items = items

    def __iter__(self):
        #iter() aplicado a la tupla crea un objeto iterador,
        # como exige el protocolo.
        return iter(self.items * self.veces)

# puedes usarlo con un for poruq el for llama
for r in Repetidor4(3, 'a', 'b', 'c'):
    print(r, end=' ')
#a b c a b c a b c
"""
En este ejemplo hemos modificado nuestra clase
Repetidor para que acepte varios elementos y los
repita de manera concatenada  
"""



"""
Tipo de objeto	 __iter__()	    __next__()	        Comentario
Iterable	      si	        no (opcional)	Puede devolver un iterador
Iterador	      si	        si	            Puede devolver y recordar el estado



####OBJETO ITERADOR####
• Iterador: Un iterador es un objeto que implementa:
__next__() → para dar el siguiente valor.
__iter__() que devuelve self → para que pueda usarse en bucles for, 
iter(), etc.
########



#####OBJETO ITERABLE######
• Iterable: 
Un objeto iterable es un objeto que devuelve un iterador. 
Para ello implementa el método __iter__.

########





"""














"""
! Sí, en ambos casos usamos iter() y next(), pero la diferencia está 
en qué tipo de objeto tenemos inicialmente.




entonces con el iterador puedo hacer la iteracion manualmente con next 
y con el iterable  debo usar un for si o si

 1. Con un iterador, puedes hacer la iteración manualmente con next()
Sí, porque el iterador tiene el método __next__().
"""
it = iter([10, 20, 30])  # esto crea un iterador a partir de una lista (que es iterable)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
try:
    print(next(it))  # StopIteration
except StopIteration:
     print("se acabo la lista")

"""
✅ 2. Con un iterable, puedes usar for, pero no estás obligado
Un iterable por sí solo no tiene __next__(), así que no puedes hacer next(iterable) directamente.
Pero puedes convertirlo en iterador usando iter():
"""

lista = [10, 20, 30]  # iterable

# for: forma automática
for x in lista:
    print(x)

# forma manual:
it = iter(lista)       # iterador creado desde el iterable
print(next(it))        # 10
print(next(it))        # 20
print(next(it))        # 30



"""
MAS EXPLICADO 
"""

print("\n caso 1\n")
#✅ CASO 1: Ya tienes un iterador
class MiIterador:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self  # es su propio iterador

    def __next__(self):
        if self.n >= 3:
            raise StopIteration
        self.n += 1
        return self.n - 1

it = MiIterador()       # ya es un iterador
print(next(it)) #0        #  SE PUEDE USAR next directo el next
print(next(it)) #1


# Aquí NO es necesario hacer iter(it) porque ya es un iterador.
#El bucle for internamente sí haría iter(it), pero eso solo devolvería
# el mismo objeto (self).

print("\n caso 2\n")
#CASO 2: Tienes un iterable

class MiIterable:
    def __iter__(self):
        return iter([10, 20, 30])  # devuelve un iterador

obj = MiIterable()

# Esto NO funcionaría:
# next(obj)  ❌ error: MiIterable no tiene __next__()

# Pero puedes hacer esto:
it = iter(obj)   # devuelve el iterador usando iter
print(next(it))  # 10    entonces si puedes usar next
print(next(it))  # 20




#En ambos casos usas next(), pero sólo sobre el iterador.
#Si tienes un iterador directo, puedes hacer next() sin más.
#Si tienes un iterable, necesitas convertirlo primero a iterador con iter().






"""
¿Qué hace realmente un for por dentro?
####Esto:

for x in objeto:
    ...
    
    
####es equivalente a:

iterador = iter(objeto)     # El for llama a __iter__()
while True:
    try:
        x = next(iterador)  # El for llama a __next__()
        ...
    except StopIteration:
        break


"""


# LOS DOS FUNCIONARIAN CON EL FOR POR
# Caso 1: El objeto ya es un iterador  tiene iter y next
for x in MiIterador():
    print(x)
#Funciona porque __iter__() devuelve self, y tiene __next__() → el for puede iterar.

#Caso 2: El objeto es un iterable   tienen iter
for x in MiIterable():
    print(x)
#Funciona porque __iter__() devuelve un iterador → el for lo usa internamente.




