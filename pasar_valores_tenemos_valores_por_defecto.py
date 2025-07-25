# definir valores por defecto en argumentos de funcion
# para no tener que pasarle alguno
def f(a, b=10, c=30):
    print(a, b, c)

f(1) # pasamos solo el arg a  falta b y c
f(1, 12) # pasamos a y b   falta c
f(1, 12, 19) # pasamos a b y c TODOS