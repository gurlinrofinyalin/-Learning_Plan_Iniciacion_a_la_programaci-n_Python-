
# paso por referencia
# se modifica dentro de la funcion
# fuera no hay modificacion
def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b

a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función