#Operadores

# Módulo Nos devuelve el resto de una división:
# %   simbolo
n_numerador = 85
n_denominador = 9
n_resto = n_numerador % n_denominador
print("El resto de dividir" , n_numerador
      , "entre" , n_denominador
      , "es" , n_resto)

# == Igual que...
# No confundir con el operador de asignación =
# Con = le damos un valor a una variable.
# Con == comprobamos si dos objetos son iguales.
n_numero1 = 34
s_texto1 = "34"
n_numero1 == s_texto1
print(n_numero1 == s_texto1)# False
n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3
print(n_numero2 == n_numero3)# True


# != Diferente que...
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5
print(n_numero4 != n_numero5)

# += Suma e incremento    primero suma
n_numero6 = 34
n_numero6 += 1 #34 +1 = 35
print(n_numero6)#35
#Sería como poner:
n_numero6 = n_numero6 +1
print(n_numero6)#  35 +1 = 36