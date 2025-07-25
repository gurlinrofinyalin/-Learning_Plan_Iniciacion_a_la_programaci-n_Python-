
"""
Pero nuestra excepción es muy básica. Vamos a
mejorarla un poco para que pueda representar su
propio mensaje de error
"""

import sys
import traceback

# clase que hereda de Exception para poder ser una excepcin
class miError(Exception):

    # constructor almacenamos el objeto
    def __init__(self, valor):
        self.valor = valor
    # el metodo magico
    # define como queremos  representar a la clase si
    # queremos mostrarla como string por print por ejemplo
    def __str__(self):
        return str(self.valor)

try:
    raise(miError('Mensaje de error'))
except miError as e:
    # sacamos los argumentos  solo tiene 1
    print(f"Argumentos de la excepción: {e.args}")
    # si tiene agumentos , muestra el primero
    if e.args:
        print(f"Mensaje específico (primer argumento): {e.args[0]}")

#Argumentos de la excepción: ('Mensaje de error',)
#Mensaje específico (primer argumento): Mensaje de error

    print("-" * 30)
    # --- Capturando la traza de la pila (stack trace) ---
    print(" usamos  sys.exc_info() que devuelve una tupla")
    print(" la tupla es (tipo_de_excepcion, objeto_excepcion, objeto_traceback)")
    print("\n--- Detalles de la traza (solo si se necesita para depuración) ---")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("exc_type:", exc_type)  # <class '__main__.miError'>
    print("exc_obj:", exc_obj)  # Mensaje de error    el mensaje puesto por nosotros
    print("exc_tb", exc_tb)  #  <traceback object at 0x7fa43b47b5c0>
    print("-" * 30)

    print(
        """ usamos traceback.format_exception() formatea la traza de forma similar \n a como la verías en la consola""")
    # usamos la tupla de antes
    formatted_trace = traceback.format_exception(exc_type, exc_obj, exc_tb)

    # numero de la linea
    numero_de_linea = exc_tb.tb_lineno
    # También podemos obtener el nombre del archivo si es necesario
    nombre_del_archivo = exc_tb.tb_frame.f_code.co_filename
    print(f"Archivo donde ocurrió el error: {nombre_del_archivo}")
    print(f"Número de línea donde se generó la excepción: {numero_de_linea}")
    """
    Archivo donde ocurrió el error: /home/death/Documents/pythonIBM/proyectos/Excepciones/Creando_Nuevas_Excepciones_Mejora.py
    Número de línea donde se generó la excepción: 24
    """



    print("\nTraza de la pila completa: ")
    for line in formatted_trace:
        sys.stdout.write(line)  # Usa sys.stdout.write para imprimir las líneas tal cual

"""  SI NO SE CAPTURA 
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Creando_Nuevas_Excepciones_Mejora.py", line 16, in <module>
    raise(miError('Mensaje de error'))
miError: Mensaje de error
"""


print("\n"*1+"@"*30)
"""
En este ejemplo hemos creado un constructor de nuestra excepción 
que utilizamos para almacenar un objeto que luego pasaremos 
al método __str__.
 
método __str__.
Este método es un método especial de Python, llamado “método mágico”. 
En concreto, __str__ define como hay que representar una clase si 
se la quiere mostrar como un string (una cadena de texto), por ejemplo,
para introducirla en un print, etc.

En este caso, el método __str__ permite mostrar el mensaje de error 
que queramos al lanzar nuestra excepción. 
"""

print("\n"*1+"@"*30)