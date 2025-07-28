
def funcion_decoradora(funcion_a_decorar):
    def funcion_interior(*args, **kwargs):
        print("calculo terminado")
        # IMPORTANT: You'll also need to call the original function here!
        funcion_a_decorar(*args, **kwargs)
    return funcion_interior # <-- Corrected: return the function object, not its result
@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def multiplica(num1, num2, num3):
    print(num1 * num2 * num3)

@funcion_decoradora
def potencia(base, exponente):
    print(base, exponente)

suma(3,5)
resta(10,5)
multiplica(2,3,4)
potencia(base=3, exponente=4)


#*args recoge argumentos posicionales en una tupla.

#**kwargs recoge argumentos de palabra clave en un diccionario.
"""
Se ponen *args y **kwargs juntos en una función (especialmente en decoradores) para 
hacerla lo más flexible y universal posible.
¿Por Qué Juntos?
Imagina que estás escribiendo un decorador que necesita envolver cualquier función, 
sin importar cómo esa función original reciba sus argumentos.

Algunas funciones solo usan argumentos posicionales:
def suma(a, b): # Necesita dos argumentos posicionales
    pass
Para que tu decorador pueda pasar a y b a suma, necesitas *args.

Algunas funciones solo usan argumentos de palabra clave:
def configuracion(host="localhost", puerto=8080): # Necesita argumentos de palabra clave
    pass
IMPORTANTE
Para que tu decorador pueda pasar host y puerto a configuracion, necesitas **kwargs.

Algunas funciones usan una mezcla:
                      posicionales *args     palabra clave *kwars
def procesar_pedido(producto, cantidad, cliente_id=None, urgente=False):
    pass
    
Esta función podría ser llamada como procesar_pedido("manzana", 5) (solo posicionales),
 o procesar_pedido("pera", 2, urgente=True) (posicionales y de palabra clave).

Si tu funcion_interior en el decorador solo tuviera *args, no podría manejar argumentos
 de palabra clave. Si solo tuviera **kwargs, no podría manejar argumentos posicionales.

Al usar *args, **kwargs juntos, la funcion_interior se vuelve un "camaleón" de argumentos:
 puede capturar y luego reenviar cualquier combinación de argumentos que la función
  original (funcion_a_decorar) espere, ya sean posicionales, de palabra clave, o una 
  mezcla de ambos.

En Resumen:
Se utilizan *args y **kwargs combinados para crear funciones genéricas (como los 
decoradores) que pueden aceptar y pasar cualquier conjunto de argumentos a otra función,
 sin tener que saber de antemano cuántos o qué tipo de argumentos serán. 
 Esto es clave para la reutilización y la flexibilidad del código en Python.

"""
