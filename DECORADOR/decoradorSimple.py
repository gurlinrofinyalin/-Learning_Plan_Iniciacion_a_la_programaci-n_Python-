"""
@mi_decorador  # ← Esto es un decorador
def mi_funcion():
    print("Hola")

# Equivale a:
mi_funcion = mi_decorador(mi_funcion)
"""