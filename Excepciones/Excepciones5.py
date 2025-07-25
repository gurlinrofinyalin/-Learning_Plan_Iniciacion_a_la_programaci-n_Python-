"""
Lanzando excepciones manualmente

Podemos lanzar excepciones directamente en nuestro código utilizando
la sentencia raise seguida del tipo de excepción que queremos lanzar.
Por ejemplo:
"""
# lanzamos la excpcion de tipo IndexError
try:
    raise IndexError
except:
    print(" cogemos todas las excepciones")

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepcion5.py", line 8, in <module>
    raise IndexError
IndexError

"""

"""
Aquí acabamos de lanzar nuestra propia excepción
de tipo IndexError. 

Eso sí, en este caso, al ver la traza del error, no tenemos 
ninguna información que nos oriente cual ha podido ser la causa del error. 
"""

"""
Si queremos añadir esa información, simplemente
creamos una instancia de IndexError (o de la
excepción que queramos lanzar) y en su constructor
añadimos el mensaje a mostrar:

"""
# si añadimos primero los modulos podemos ver mas detalles de la excepcion
import sys
import traceback
# añadimos en el constructor el mensaje  al lanzar con raise
try: # si no la capturamos no puede llegar el sigueinte codigo de abajo
    raise IndexError('Excepción lanzada manualmente')
except IndexError as e:
    # 'e' es el objeto de la excepción que contiene el mensaje y otros detalles.
    print("\n¡Se ha capturado un IndexError! esto puesto manualmente")
    print(f"Mensaje de la excepción: {e}")
    # Puedes convertir 'e' a cadena para ver el mensaje.
    # Alternativamente, puedes acceder a los argumentos de la excepción,
    # donde el primer argumento suele ser el mensaje principal.
    print(f"Argumentos de la excepción: {e.args}")
    if e.args:
        print(f"Mensaje específico (primer argumento): {e.args[0]}")


    print("-"*30)
    # --- Capturando la traza de la pila (stack trace) ---
    print(" usamos  sys.exc_info() que devuelve una tupla")
    print(" la tupla es (tipo_de_excepcion, objeto_excepcion, objeto_traceback)")
    print("\n--- Detalles de la traza (solo si se necesita para depuración) ---")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("exc_type:",exc_type)#<class 'IndexError'>
    print("exc_obj:",exc_obj)#Excepción lanzada manualmente
    print("exc_tb",exc_tb)#<traceback object at 0x7fdee5ca02c0>
    print("-"*30)

    print(""" usamos traceback.format_exception() formatea la traza de forma similar \n a como la verías en la consola""")
    # usamos la tupla de antes
    formatted_trace = traceback.format_exception(exc_type, exc_obj, exc_tb)

    # numero de la linea
    numero_de_linea = exc_tb.tb_lineno
    # También podemos obtener el nombre del archivo si es necesario
    nombre_del_archivo = exc_tb.tb_frame.f_code.co_filename
    print(f"Archivo donde ocurrió el error: {nombre_del_archivo}")
    print(f"Número de línea donde se generó la excepción: {numero_de_linea}")
    """
    Archivo donde ocurrió el error: /home/death/Documents/pythonIBM/proyectos/Excepciones/Excepcion5.py
    Número de línea donde se generó la excepción: 42
    """


    print("\nTraza de la pila completa: ")
    for line in formatted_trace:
        sys.stdout.write(line)  # Usa sys.stdout.write para imprimir las líneas tal cual
"""   SIN CAPTURAR
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepcion5.py", line 8, in <module>
    raise IndexError
IndexError
"""

""" CAPTURANDO 
¡Se ha capturado un IndexError! esto puesto manualmente
Mensaje de la excepción: Excepción lanzada manualmente
Argumentos de la excepción: ('Excepción lanzada manualmente',)
Mensaje específico (primer argumento): Excepción lanzada manualmente
------------------------------
 usamos  sys.exc_info() que devuelve una tupla
 la tupla es (tipo_de_excepcion, objeto_excepcion, objeto_traceback)

--- Detalles de la traza (solo si se necesita para depuración) ---
exc_type: <class 'IndexError'>
exc_obj: Excepción lanzada manualmente
exc_tb <traceback object at 0x7fdee5ca02c0>
------------------------------
 usamos traceback.format_exception() formatea la traza de forma similar 

     a como la verías en la consola
Traza de la pila completa: 
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepcion5.py", line 42, in <module>
    raise IndexError('Excepción lanzada manualmente')
IndexError: Excepción lanzada manualmente
"""





print("\n"*1+"@"*30)
"""
Ahora sí, vemos que en la última línea del error
tenemos el mensaje explicativo del error.
Por supuesto, es posible capturar nuestras propias
excepciones lanzadas manualmente:
"""
try:
    raise IndexError('Excepción lanzada manualmente')
except:
    print('He capturado mi pripia excepción')
"""
He capturado mi pripia excepción
"""


print("\n"*1+"@"*30)
try:
    # Lanzamos una excepción IndexError manualmente con un mensaje personalizado
    raise IndexError('¡Mi excepción de índice personalizada ha sido lanzada!')
except IndexError as error_personalizado:
    print("\n¡Se ha capturado mi IndexError personalizado!")
    print(f"Mensaje del error: {error_personalizado}")
    print(f"Tipo del error: {type(error_personalizado)}")

print("\n--- El programa continúa normalmente. ---")

"""
He capturado mi pripia excepción
##############################

¡Se ha capturado mi IndexError personalizado!
Mensaje del error: ¡Mi excepción de índice personalizada ha sido lanzada!
Tipo del error: <class 'IndexError'>

--- El programa continúa normalmente. ---
"""