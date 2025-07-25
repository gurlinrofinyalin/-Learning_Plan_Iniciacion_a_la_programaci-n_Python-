
# Calcula la raiz cuadrada de un número.
# Tenemos tres intentos y el número no puede ser negativo.

import math;
intentos=0;
num = int(input("Introduce numero: "))

while num<0:
    intentos=intentos+1
    print("Incorrecto")
    num=int(input("Introduce numero: "))
    if intentos==2:
        print("Demasiados intentos")
        break;

# como esto solo lo hace cuando los intentos son menores de 2
# nunca  va a provocar error porque no va a calcular la raiz
# si no das en las dos primeras veces una numero correcto
if intentos < 2:
    intentos = intentos + 1
    solucion = math.sqrt(num)
    print("la raiz cuadrada de "+str(num)+ " es: "+str(solucion))