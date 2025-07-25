#El bucle while

# WHILE

# Imprime edad cuando el contador llegue a 18
edad = 0
while edad < 18:
    edad=edad+1
print("Tienes "+str(edad))
# sale con 18 porque no se cumple la condicion para volver

print("-----------------\n---------------")
# Pregunta la edad mientras sea negativa
edad=int(input("Introduce edad: "))
while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))
print("tu edad es: "+str(edad))
"""
Introduce edad: -3
Edad incorrecta
Introduce edad: 18
tu edad es: 18
-----------------
"""
print("-----------------\n---------------")



# Bucle while con un if anidado y un break
    # Salga del bucle cuando num sea 3:
num = 1
while num < 6:
    print(num)
    if num == 3:
        break
    num += 1

"""
1
2
3
"""