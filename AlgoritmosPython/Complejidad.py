#Genero una lista de 100 millones de números aleatorios
import time
import numpy as np
x = list(np.random.randint(low=1,high=500000, size=99999999))


#Complejidad Constante O(k) Constant Time
# %%time solo en Jupyter Notebooks  JupyterLab
def constante(x:list) -> list:
    return x

start_time = time.time() # Guarda el tiempo de inicio
constante(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
"""
Wall time: 0 ns
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048…
"""


#Complejidad O(n) Linear Time %%time
def iterador_normal(x:list) -> list:
    contador = len(x)
    while(contador > 0):
        contador -= 1
    return x


start_time = time.time() # Guarda el tiempo de inicio
iterador_normal(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
"""
Wall time: 5.31 s
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048…
"""



#Complejidad O(n al cuadrado) Quadratic Time
# %%time solo en Jupyter Notebooks  JupyterLab
def iterador_anidado(x:list) -> list:
    contador_externo = len(x)//1000
    contador_interno = len(x)//1000
    while(contador_externo > 0):
        contador_externo -= 1
        for i in range(contador_interno):
            i
    return x


start_time = time.time() # Guarda el tiempo de inicio
iterador_anidado(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
"""
Wall time: 5min 29s
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048,
311380…
"""

"""
Constante (O(k)) - Tiempo de ejecución: 1.2636184692382812e-05 segundos
Constante (O(k)) - Tiempo de ejecución: 4.69750714302063 segundos
Constante (O(k)) - Tiempo de ejecución: 277.86167883872986 segundos
Constante (O(k)) - Tiempo de ejecución: 8.344650268554688e-06 segundos
Constante (O(k)) - Tiempo de ejecución: 1.9788742065429688e-05 segundos
Constante (O(k)) - Tiempo de ejecución: 0.0001246929168701172 segundos
Constante (O(k)) - Tiempo de ejecución: 11.141118049621582 segundos

Process finished with exit code 0

"""




#Complejidad O(log(n)) Logarithmic Time
# %%time solo en Jupyter Notebooks  JupyterLab
def iterador_multiplicado(x:list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= incremento
        incremento *= (incremento + 1)
    return x


start_time = time.time() # Guarda el tiempo de inicio
iterador_multiplicado(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
"""
Wall time: 0 ns
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048…
"""




#Complejidad O(log(n)) Logarithmic Time
# %%time solo en Jupyter Notebooks  JupyterLab
def iterador_dividido(x:list) -> list:
    iterador = -len(x)
    incremento = 1
    while(iterador < 0):
        iterador /= incremento
        incremento += 1
    return x

start_time = time.time() # Guarda el tiempo de inicio
iterador_dividido(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")

"""
Wall time: 0 ns
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048,
311380…
"""



#Complejidad O(log(log(n))) Logarithmic from Logarithmic Time
# %%time solo en Jupyter Notebooks  JupyterLab
import math
def iterador_incremento_exponencial(x:list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= pow(incremento, 2)
        incremento += 1
    return x

start_time = time.time() # Guarda el tiempo de inicio
iterador_incremento_exponencial(x)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
"""
Wall time: 0 ns
[470443,
337976,
383958,
404514,
383032,
427315,
473003,
225481,
169894,
475938,
15745,
210740,
124051,
192964,
347048…
"""



#Cálculo de la complejidad Algorítmica del Ejemplo
y = list(np.random.randint(low=1,high=500000, size=999))

# %%time solo en Jupyter Notebooks  JupyterLab
def calculo_bit_o_ejemplo(y:list) ->str:
        iterador = -len(y) # k
        incremento = 1 # k
        q_list = y # k
        while(iterador < 0): # log(n)
            iterador /= incremento # k
            incremento += 1 # k
        for p in y: # n
            for q in y: # n -> n * n
                for r in y: # n -> n * n * n
                    r
        return "La Complejidad es n*n*n, n cubo"


start_time = time.time() # Guarda el tiempo de inicio
calculo_bit_o_ejemplo(y)
end_time = time.time()   # Guarda el tiempo de finalización
print(f"Constante (O(k)) - Tiempo de ejecución: {end_time - start_time} segundos")
#Wall time: 14.7 s
#'La Complejidad es n*n*n, n cubo'