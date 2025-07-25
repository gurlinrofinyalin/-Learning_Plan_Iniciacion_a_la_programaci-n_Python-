def f(a, *, b, c): # Define 'b' y 'c' como keyword-only con el *
    print(a, b, c)

f(1, b=10, c=100)#  debemos pasar b y c por clave

# a aprtir del * los argumentos de la derecha , se tienen que pasar por clave

f(1, 10, 100) # Error al no pasar argumentos Keyword-only en b y c