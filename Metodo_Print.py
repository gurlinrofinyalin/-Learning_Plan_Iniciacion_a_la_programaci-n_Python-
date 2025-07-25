# Salida de datos .print()


#Salida de directa de datos
print("En esta ocasión hemos imprimido por pantalla este string")

#Salida de datos calculados
n_numero_1 = 4
n_numero_2 = 6
print("El resultado de sumar" , n_numero_1, "y" , n_numero_2 , "es" , (n_numero_1+n_numero_2))

"""
#Si concatenamos int y strings usando el signo + nos puede dar problemas.
print("El resultado de sumar " + n_numero_1
      + " y " + n_numero_2 + " es " + (n_numero_1+n_numero_2))

Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Metodo_Print.py", line 14, in <module>
    print("El resultado de sumar " + n_numero_1
          ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
"""
# usando {} en las variables
# sin usar + para concatenar , ni las comillas
print(f"El resultado de sumar {n_numero_1} + {n_numero_2}  es {n_numero_1+n_numero_2}")


print("El resultado de sumar" + " " + " os numeros")