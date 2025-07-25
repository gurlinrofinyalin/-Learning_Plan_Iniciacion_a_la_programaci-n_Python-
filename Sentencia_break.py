''' Bucles y las sentencias continue,

break, pass y los bloques else

sentencias que nos permiten alterar el flujo natural de los mismos.
Éstas son las siguientes sentencias:
• break: Interrumpe el flujo y sale fuera de bucle.
• continue: Salta al comienzo de la siguiente iteración del bucle.
• pass: No hace nada. Es una sentencia vacía.
• Else: Al finalizar un bucle: Se ejecuta sólo si el bucle ha
finalizado con normalidad. Es decir, se ejecuta si el bucle finaliza
sin haber ejecutado un break.


Sentencia break

Como vemos, esta sentencia interrumpe inmediatamente el bucle
y sale a la siguiente sentencia del código.

Notemos que en este caso la expresión que estamos
evaluando es la propia variable a.
Esto puede parecer raro al principio, pero es una forma muy elegante
de evaluar expresiones en este tipo de sentencias.
Tened en cuenta que en el while siempre se evalúa
una expresión booleana. Es decir, que en realidad
estamos evaluando bool(a) que, al ser a un entero,
devuelve siempre True hasta que a sea 0. Veremos
este tipo de expresiones muy frecuentemente en
Python.
'''
a = 5

#estamos evaluando bool(a) que, al ser a un entero,
#devuelve siempre True hasta que sea 0
while a: # Utilizamos la propia variable como condición
    print (a, end=' ')
    if a == 2:
        break #• break: Interrumpe el flujo y sale fuera de bucle.
    a -= 1  # a = a-1

print ('\nFuera del Bucle.')
print('Valor de "a": {}'.format(a))
#5 4 3 2    cuando llega al 2 sale y ya no resta

print(a)# 2
