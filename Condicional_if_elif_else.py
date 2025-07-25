#Conditional if…elif…else
# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.
notaIn=int(input("Introduzca nota:"))
if notaIn<5:
    calificacion="Suspenso"
else:
    calificacion="Aprobado"
print(calificacion)
print("-----------------\n---------------")
# IF no sólo evalúa un boleano, también si una variable contiene información
print(bool(-19))
variable = -19  # como es un numero es TRUE no ser que sea 0  que seria FALSE
if variable:
    print("Contiene información")
else:
    print("No contiene información")
print("-----------------\n---------------")
#En este ejemplo sí evalúa un boleano
variable = 19
if variable == True:  # 19 es un entero es True
    print("Contiene información")
else:
    print("No contiene información")
print("-----------------\n---------------")
# Programa que pide una edad por consola y valora si el usuario es mayor de edad o no.
edad=int(input("Introduce edad: ")) # varias opciones
if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")


print("-----------------\n---------------")
# Programa que pide una nota por consola y valora las posibles calificaciones del alumno.
nota=int(input("Introduce tu nota: "))
if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else: # por defecto
    print("Sobresaliente")

print("-----------------\n---------------")
# IF abreviado
n_num1 = 5
n_num2 = 10
# if condicion:  instruccion si se cumple la condicion
if n_num1 > n_num2: print(n_num1 , "es mayor que" , n_num2)

print("-----------------\n---------------")
# IF...ELSE abreviado
a = 2
b = 330
#instruccion si se cumple la condicion    if  condicion  else  condicion si no se cumple
print("A") if a > b else print("B")
print("-----------------\n---------------")
# Se pueden concatenar operadores de comparación:
edad=117
if 0 < edad < 100: # Sería como poner: if edad > 0 and edad <100
    print("Edad correcta")
else:
    print("Edad incorrecta")

print("-----------------\n---------------")
# Otro ejemplo de operadores de comparación concatenados
salarioPresidente = int(input("Introduce salario presidente: "))
print("El salario del presidente es de" , salarioPresidente)

salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" , salarioDirector)


salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" , salarioJefe)

salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" , salarioOperario)


if salarioOperario < salarioJefe < salarioDirector < salarioPresidente:
    print("Todo ok")
else:
    print("Algo no va bien")

print("-----------------\n---------------")
# Operadores AND y OR
distancia = int(input("Introduce distancia: "))
numHermanos = int(input("Introduce número de hermanos en el centro: "))
notaMedia = int(input("Introduce notaMedia: "))
if distancia > 20 or numHermanos < 2 or notaMedia <= 5:
    print("NO eres candidato a la beca")
else:
    print("Sí eres candidato a la beca")


print("-----------------\n---------------")
# Operador IN
opcion = input("ELige opcion: opcion1, opcion2, opcion3, opcion4: ")
pasoMinusculas = opcion.lower()
if pasoMinusculas in("opcion1", "opcion2", "opcion3", "opcion4"):
    print("Opción válida: " + pasoMinusculas)
else:
    print("Opción inválida: " + pasoMinusculas)

print("-----------------\n---------------")
# If anidados. Queremos comprar un coche. Necesitamos ser mayores de edad y tener 20000€
n_edad = int(input("Introduzca su edad: "))
n_dinero = int(input("Introduzca presupuesto: "))
if n_edad < 18:
    print("No tienes la edad suficiente para conducir.")
else:
    if n_dinero < 20000:
        print("Tienes la edad pero no el dinero para comprar el coche.")
    else:
        print("Puedes comprar el coche.")