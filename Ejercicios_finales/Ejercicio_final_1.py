#1. Dados dos números, escriba un código Python para encontrar el
# mínimo de estos dos números
def minimum(a,b):
    if a<=b:
        return a
    else:
        return b
a=2; b=4
print(minimum(a,b))#2
a=-1; b=-4
print(minimum(a,b))#-4


#2. Invertir palabras de una cadena dada.
# entrada
#str = código de práctica de prueba de geeks
# salida
#str = geeks de prueba de práctica de código


def rev_sentence(sentence):
    words = sentence.split(' ')
    print(words)# ['geeks', 'quiz', 'practice', 'code']
    reverse_sentence =''.join(reversed(words))
    print(reverse_sentence)#codepracticequizgeeks
    return reverse_sentence
if __name__ == "__main__":
    #  NO  se ejecuta si es un modulo importado
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

"""
¿Qué quiere decir if __name__ == "__main__":?
Este bloque es una construcción estándar en Python que sirve para determinar si un 
script se está ejecutando directamente (como programa principal) 
o si está siendo importado como un módulo por otro script.


__name__: Esta es una variable especial (integrada) en Python. 
SCRIPT EJECUTADO
Cuando ejecutas un script de Python, el intérprete asigna un valor a esta 
variable __name__ para ese script en particular:

__name__ es __main__ 
Si el script es el programa principal que se está ejecutando (es decir, lo 
ejecutas directamente desde la línea de comandos, por ejemplo, 
con python tu_script.py), Python le asigna a __name__ el valor de la cadena 
de texto "__main__".

__name__ es  nombre_del_modulo
Si el script está siendo importado como un módulo en otro script (por ejemplo, 
tienes mi_modulo.py y en otro archivo haces import mi_modulo), 
Python le asigna a __name__ el nombre del módulo (en este caso, "mi_modulo").


"__main__": Esta es la cadena de texto específica que __name__ contendrá cuando 
el script sea el que se está ejecutando como el programa principal.

if __name__ == "__main__":: Esta es una declaración condicional que verifica si 
el script actual se está ejecutando directamente.

Si la condición es verdadera: 
El código dentro de este bloque if se ejecutará. 
Aquí es donde normalmente colocas la lógica principal de tu script que quieres 
que se ejecute cuando se utiliza como un programa independiente 
(como llamar funciones, configurar datos iniciales o ejecutar pruebas).

Si la condición es falsa: El código dentro de este bloque if no se ejecutará. 
Esto ocurre cuando el script es importado como un módulo. 
Esto te permite definir funciones, clases y variables en un módulo que pueden 
ser reutilizadas por otros scripts sin que se ejecute automáticamente 
la parte "principal" del código de ese módulo.

¿Por qué se utiliza?
Esta construcción es fundamental para crear código reutilizable.
 Permite que un archivo Python tenga un doble propósito:

Script Ejecutable: 
Cuando lo ejecutas directamente, realiza una tarea específica
 (por ejemplo, en tu código, se llama a la función rev_sentence con una entrada
  de prueba).

Módulo Importable: 
Cuando otro script lo importa, solo carga las definiciones 
(funciones, clases, variables), pero no ejecuta la lógica principal, 
lo que evita efectos secundarios no deseados.


"""















#3. Realizar una suma de los elementos de una tupla


#
#
#
# 4. Escriba un código que calcule una lista de números proporcionados.
#
#
#
# 5. Escriba un código que desordene al azar una lista.
#
#
#
# 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.
#
#
#
# 7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?
#
# Solución:"-1" siempre se refiere al último índice de la lista, por lo tanto, la respuesta seria 3.
#
# 8. Escriba un programa para producir la serie Fibonacci en Python.
#
#
#
# 9. Escriba un programa en Python para comprobar si un número es primo.
#
#
#
# 10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.
#
#
#
# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
#
#
#
# 12. ¿Cuál de las siguientes declaraciones es inválida?
#
# a) abc = 1.000.000
#
# b) a b b c = 1000 2000 3000
#
# c) a,b,c = 1,000,000
#
# d) a_b_c = 1,000,000
#
# Solución: b) a b b c = 1000 2000 3000
#
# Porque en los nombres de variables, no se permiten espacios.
#
# 13. ¿Cuál es el resultado de ejecutar el siguiente código?
#
#
#
# a) Se ha producido algún error
#
# b) No se ha producido algún error
#
# c) Código inválido
#
# d) Ninguno de los anteriores
#
# Solución: c) código inválido
#
# 14. ¿Como se puede acceder al último índice de una lista?
#
# Respuesta: Supongamos que la lista1 es [2, 33, 222, 14, 25], Entonces mediante, lista1 [-1] obtendremos el ultimo índice de la lista. Es decir, 25.