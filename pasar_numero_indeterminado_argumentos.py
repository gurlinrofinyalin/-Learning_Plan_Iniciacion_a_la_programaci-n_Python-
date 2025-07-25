


'''
 *args y **kwargs en Python
En Python, cuando defines una función, a veces no sabes de antemano cuántos argumentos
le vas a pasar. Para manejar esto, Python te ofrece dos sintaxis especiales:
*args y **kwargs.

*args (Argumentos Posicionales Arbitrarios)
El asterisco simple (*) antes de un nombre de parámetro (por convención se usa args,
pero podrías usar cualquier otro nombre) sirve para que la función acepte un número
arbitrario de argumentos posicionales.
Esto significa que puedes pasarle tantos argumentos como quieras,
y Python los recogerá todos en una tupla.

 '''
# args se puede sustituir por otro  nombre es una conveniencia
def f(*args): # Acepta número arbitrario de argumentos
    print(args) # devuelve tupla , si no hay agumentos devuelve tupla vacia
    print("Tipo de 'args':", type(args))# Tipo de 'args': <class 'tuple'>

f() # Si no hay argumentos, args es una tupla vacía
#()
#Tipo de 'args': <class 'tuple'>

f(1)
#(1,)
#Tipo de 'args': <class 'tuple'>

f(1, 2)
#(1, 2)
#Tipo de 'args': <class 'tuple'>

f(1, 2, 3, 4, 5, 6)
#(1, 2, 3, 4, 5, 6)
#Tipo de 'args': <class 'tuple'>




'''
**kwargs (Argumentos de Palabra Clave Arbitrarios)
El doble asterisco (**) antes de un nombre de parámetro (por convención se usa kwargs, 
pero de nuevo, podrías usar otro nombre) sirve para que la función acepte un número
 arbitrario de argumentos de palabra clave (o argumentos nombrados). 
 Python los recogerá todos en un diccionario. 
 Las claves de este diccionario serán los nombres de los argumentos de palabra clave 
 que pasaste, y los valores serán los valores correspondientes.
'''

# kwargs se puede sustituir por otro nombre es una conveniencia
                            # 'opciones' capturará todos los argumentos de palabra clave
                            # devuelve un DICCIONARIO
                            # donde los nombres de los argumentos pasados son la clave
                            # donde los valores de los argumentos pasados son el valor
def configurar_perfil(**opciones): # Acepta número arbitrario de argumentos

    print("Tipo de 'opciones':", type(opciones))
    print("Las configuraciones recibidas son:", opciones)

    # si la palabra clave "nombre" se manda como argumento imprime el valor
    # osease Ana
    if "nombre" in opciones:
        print(f"El nombre del usuario es: {opciones['nombre']}")
    # si la palabra clave "edad" esta en opciones imprime el valor
    # osease 28
    if "edad" in opciones:
        print(f"La edad es: {opciones['edad']}")
    # si la palabra clave "ciudad" esta en opciones imprime el valor
    # osease nada porque no esta
    if "ciudad" in opciones:
        print(f"La ciudad es: {opciones['ciudad']}")



configurar_perfil(nombre="Ana", edad=28) # Pasamos dos argumentos de palabra clave
# Tipo de 'opciones': <class 'dict'>
# Las configuraciones recibidas son: {'nombre': 'Ana', 'edad': 28}
# El nombre del usuario es: Ana
# La edad es: 28

configurar_perfil(producto="Libro", precio=25.50, stock=True) # 3 s argumentos
# Tipo de 'opciones': <class 'dict'>
# Las configuraciones recibidas son: {'producto': 'Libro', 'precio': 25.5, 'stock': True}

configurar_perfil() # No pasamos ningún argumento de palabra clave
# Tipo de 'opciones': <class 'dict'>
# Las configuraciones recibidas son: {}
# Como puedes observar, **opciones convierte todos los argumentos de palabra clave pasados en un diccionario llamado opciones dentro de la función. Esto es extremadamente útil cuando quieres crear funciones muy flexibles que pueden aceptar diferentes configuraciones o parámetros sin tener que definir un parámetro individual para cada uno.





#OTRO EJEMPLO DE KARGS

def f(**Kargs): # Acepta número de argumentos por nombre
    print(Kargs)


f() # Si no hay argumentos, Kargs es un diccionario vacío
#{}
f(a=1)
#{'a': 1}
f(a=1, b=2)
#{'a': 1, 'b': 2}
f(a=1, c=3, b=2)
#{'a': 1, 'c': 3, 'b': 2}

