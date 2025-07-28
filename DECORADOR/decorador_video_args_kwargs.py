def funcion_decoradora(funcion_a_decorar):
    print("EMPIEZA funcion decoradora ")

    def funcion_interior():
        print("Empieza funcion interior ")
        funcion_a_decorar()  # funcion_a_decorar es suma o resta
        print("Fin funcion interior ")
        # Don't call funcion_interior here. Just return it.

    print("FIN funcion decoradora ")
    return funcion_interior # <-- Corrected: return the function object


#El decorador funcion_decoradora recibe como argumento la función que está
# "decorando" en ese momento.  en este caso suma
@funcion_decoradora
def suma():
    print(15+20)

#@funcion_decoradora # Uncommented for demonstration
def resta():
    print(30-10)

suma()
print("---") # Added to separate outputs
resta()

# un decorador es una funcion que se le añade a  otra funcion

"""
Entendiendo el Error en Tu Decorador
un error TypeError: 'NoneType' object is not callable debido a la forma en que 
tu función funcion_decoradora está estructurada, específicamente en la instrucción 
return dentro de funcion_interior.



Los decoradores envuelven funciones: 
Cuando usas @funcion_decoradora encima de suma(), 
Python internamente hace algo como suma = funcion_decoradora(suma).

Lo que un decorador debe devolver: 
Una función decoradora siempre debe devolver un objeto que pueda ser llamado 
(normalmente otra función, 
como funcion_interior en tu caso) que reemplazará a la función original decorada.

El problema en funcion_interior:

Python

def funcion_interior():
    print("Empieza funcion interior ")
    funcion_a_decorar()
    print("Fin funcion interior ")
    return funcion_interior() # <-- ¡Este es el culpable!
Aquí, return funcion_interior() provoca una recursión infinita. funcion_interior se llama a sí misma repetidamente. Eventualmente, se alcanzaría el límite de recursión de Python. Lo más importante es que, al intentar return funcion_interior(), la función funcion_interior se ejecuta, y cuando una función no devuelve explícitamente un valor, implícitamente devuelve None. Así, después de la primera llamada a funcion_interior dentro de suma(), funcion_interior() intenta llamar a None, lo que lleva al TypeError: 'NoneType' object is not callable. No puedes llamar a None como si fuera una función.
"""


