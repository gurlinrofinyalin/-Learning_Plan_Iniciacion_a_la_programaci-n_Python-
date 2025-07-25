#Sentencia continue
#La sentencia continue nos permite interrumpir la iteración actual

"""
sentencias que nos permiten alterar el flujo natural de los mismos.
Éstas son las siguientes sentencias:
• break: Interrumpe el flujo y sale fuera de bucle.
• continue: Salta al comienzo de la siguiente iteración del bucle.
• pass: No hace nada. Es una sentencia vacía.
• Else: Al finalizar un bucle: Se ejecuta sólo si el bucle ha
finalizado con normalidad. Es decir, se ejecuta si el bucle finaliza
sin haber ejecutado un break.
"""


a = 7 # comieza
print(bool(a))#True

while bool(a): # mientras a no sea 0 que sera False, es True
    a -= 1 # a = a - 1
    if a % 2 == 0: # cuando a sea divisible por 2, saltamos
        continue # Saltamos a la siguiente iteracción si es a es par.
    print (a, end=' ')# no se ejecuta si sale
# como empieza por 7

print ('\nFuera del Bucle.')

#5 3 1
