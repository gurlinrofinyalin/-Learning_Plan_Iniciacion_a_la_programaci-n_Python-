def log1(*args):
    print("LOG:", *args)
log1(2,3,"idiota")
print('-----')

def log2(*args, prefix):
    print(prefix, *args)
    # se coloca los que se pasan por clave al final
log2(2,3,"idiota",prefix="elemento")
print('-----')

def log3(*args, sep, prefix):
    print(prefix, *args, sep=sep)
log3("Este", "es", "otro", "mensaje", prefix="DEBUG:", sep=" - ")
print('-----')

def log4(*args, sep=" ", prefix="LOG:"):
    print(prefix, *args, sep=sep)
log4("Este", "es", "otro", "mensaje")
print('-----')

def log5(*args, prefix="LOG:",sep):
    print(prefix, *args)
log5("Este", "es", "otro", "mensaje", sep=" | ")
print('-----')

def log6(*args, sep=" ", prefix="LOG:"):
    print(prefix, *args, sep=sep)

# Diccionario de ejemplo
diccionario = {
    "prefix": "INFO:",             # el prefijo
    "sep": " | "                   # el separador
}

# Llamada desempaquetando el diccionario
log6("Mensaje", "importante", "aquí", **diccionario)

print('-----')


