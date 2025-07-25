#Creando nuestras propias excepciones

"""
Hasta ahora hemos visto como capturar y lanzar excepciones incluidas
en la librería estándar de Python.

Sin embargo, en muchos casos es de gran utilidad crear nuestras propias
excepciones.

Si no os habíais fijado hasta ahora, las excepciones son clases.

Por eso, si queremos crear nuestra propia excepción, sólo tenemos que
crear una clase que herede de la clase base de todas las excepciones
(Exception) o de cualquier otra excepción:
"""


# Las excepciones heredan de Exception
class miPropiaExcepcion(Exception):
    pass

try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print("se captura nuestra propia excepcion miPropiaExcepcion")

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Creando_Nuevas_Excepciones.py", line 30, in <module>
    raise miPropiaExcepcion
miPropiaExcepcion
"""

"""
Acabamos de crear la clase MiPropiaExcepcion que
hereda de Exception. Cuando una clase hereda de
Exception, podemos incluirla dentro de una sentencia
raise para lanzarla, así como dentro de un except para
interceptarla
"""
print("\n"*1+"@"*30)


