#POR POSCION args
def mostrar_elementos(*args):
    return args[0],args[1],args[2],args[3]
datos_completos = [10, 20, 30, 40]
print(type(datos_completos))# una list
e1, e2, e3, e4 = mostrar_elementos(*datos_completos)
print(f"Elemento 1: {e1}")
print(f"Elemento 2: {e2}")
print(f"Elemento 3: {e3}")
print(f"Elemento 4: {e4}")

print('-------------------------------------------')

#POR CLAVE  kargs


def funcion_desempaquetar_valores(**kwargs):
    valores = list(kwargs.values())  # Convertir valores a lista

    # Asignar a variables (suponiendo que sabemos cuántos elementos hay)
    if len(valores) >= 4:
        var1, var2, var3, var4 = valores[0], valores[1], valores[2], valores[3]
    else:
        var1 = var2 = var3 = var4 = None  # Valores por defecto

    print(f"Variables desempaquetadas: {var1}, {var2}, {var3}, {var4}")
    return var1, var2, var3, var4  # Devolver como tupla


# Uso con argumentos arbitrarios
a, b, c, d = funcion_desempaquetar_valores(x=10, y=20, z=30, nombre="Python")
print("Fuera de la función:", a, b, c, d)

print('-------------------------------------------')

def f(a,b,c,d):
    return a,b,c,d# aqui  estan desempaquetados

argumentos = {'b':20, 'a':1, 'c':300,'d':4000}
print(type(argumentos))#<class 'dict'>   diccionario
a, b, c, d = f(**argumentos) # Desempaquetando diccionario argumentos con **
print(a)
print(b)
print(c)
print(d)
'''
1
20
300
4000
<class 'dict'>
'''
print('-------------------------------------------')
argumentos2 = {'b':200, 'c':300, 'd':400}
print(type(argumentos2))#<class 'dict'>   diccionario
a, b, c, d = f(10, **argumentos2) # Podemos combinar argumentos posicionales con dict
print(a)
print(b)
print(c)
print(d)
'''
10
200
300
400
'''

print('-------------------------------------------')
def funcion_variable_kwargs(**kwargs):
    print("Argumentos recibidos:", kwargs)
    return kwargs

resultado = funcion_variable_kwargs(x=10, y=20, z=30, nombre="Python")
print(type(resultado))
print(resultado)
print(resultado['x'])

