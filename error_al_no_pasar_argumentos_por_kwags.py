def f(a, *b, c): # Hay que pasar 'c' por clave obligatoriamente
    print(a, b, c)

# se tiene que pasar c por clave  sino error

# sin contar bm se tienen que pasar los argumentos a la derecha de b
# por clave, b no cuenta porque tiene el asterisco *

f(1, c=2)
f(1, 2, c=3)
f(1, 2, 3, 4, 5, c=10) 


