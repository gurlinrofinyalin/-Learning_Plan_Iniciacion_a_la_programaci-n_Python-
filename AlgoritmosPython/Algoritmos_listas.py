"""
https://www.bigocheatsheet.com/
tablas

Este algoritmo busca un elemento en un array
ordenado dividiendo el array en 2 mitades, identifica
en cuál de las mitades se encuentra, luego divide esa
parte en 2 mitades iguales y busca nuevamente hasta
encontrar el elemento, es un algoritmo recursivo:
"""
def bin(a,x,low,high):
    ans = -1
    if low==high: ans = -1
    # el rango de busqueda se reduce a un elemento
    # x no es a[low] ni  x es igual a a[high]
    # el elemento no esta , se devuelve -1 por conveccion
    else:
        """Es la condición que se activa cuando el algoritmo encuentra  el elemento que está buscando.
        Cuando el algoritmo ejecuta la línea mid = (low + ((high - low) // 2)), 
        calcula el índice del elemento central en la porción actual del arreglo  que está examinando.
        Luego, tiene tres posibles ramas condicionales:
        
        if x < a[mid]: Si el elemento buscado (x) es menor que el elemento en el medio (a[mid]), 
        significa que x debe estar en la mitad izquierda del segmento.
        
        elif x > a[mid]: Si el elemento buscado (x) es mayor que el elemento  en el medio (a[mid]), 
        significa que x debe estar en la mitad derecha del segmento.
        
        else: ans = mid ¡Aquí es donde entramos!  
        Si ninguna de las dos condiciones anteriores es verdadera 
        (es decir, x no es menor que a[mid] y x no es mayor que a[mid]),
         la única posibilidad que queda es que x sea igual a a[mid].
        """
        mid = (low+((high-low)//2)) # divide entre 2
        if x < a[mid]: ans = bin(a,x,low,mid) # mitad mas baja
        elif x > a[mid]: ans = bin(a,x,mid+1,high) # mitad mas alta
        else: ans = mid
    return ans


a = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91,
     105, 110, 115, 120, 125, 130, 135, 140, 145, 150,
     155, 160, 165, 170, 175, 180, 185, 190, 195, 200,
     205, 210, 215, 220, 225, 230, 235, 240, 245, 250,
     255, 260, 265, 270, 275, 280, 285, 290, 295, 300,
     305, 310, 315, 320, 325, 330, 335, 340, 345, 350,
     355, 360, 365, 370, 375, 380, 385, 390, 395, 400,
     405, 410, 415, 420, 425, 430, 435, 440, 445, 450,
     455, 460, 465, 470, 475, 480, 485, 490, 495, 500]
# busca x que es 265
# el array es de 100, asique low es 0 y high es 100
bin(a, 265, 0, 100)



"""
Initial Call: bin(a, 265, 0, 100) 
(where low = 0 and high = 100 because the array has 101 
elements from index 0 to 100)

mid = (0 + ((100-0)//2)) = 50
la mitad es 50  de 100 elementos

a[50] is 305. Since 265 < 305, the search continues in the left half.

Recursive call: bin(a, 265, 0, 50)

Second Call: bin(a, 265, 0, 50)

mid = (0 + ((50-0)//2)) = 25

a[25] is 180. Since 265 > 180, the search continues in the right half.

Recursive call: bin(a, 265, 26, 50) (Note: mid + 1 for the new low)

Third Call: bin(a, 265, 26, 50)

mid = (26 + ((50-26)//2)) = 26 + 12 = 38

a[38] is 250. Since 265 > 250, the search continues in the right half.

Recursive call: bin(a, 265, 39, 50)

Fourth Call: bin(a, 265, 39, 50)

mid = (39 + ((50-39)//2)) = 39 + 5 = 44

a[44] is 275. Since 265 < 275, the search continues in the left half.

Recursive call: bin(a, 265, 39, 44)

Fifth Call: bin(a, 265, 39, 44)

mid = (39 + ((44-39)//2)) = 39 + 2 = 41

a[41] is 260. Since 265 > 260, the search continues in the right half.

Recursive call: bin(a, 265, 42, 44)

Sixth Call: bin(a, 265, 42, 44)

mid = (42 + ((44-42)//2)) = 42 + 1 = 43

a[43] is 265. Success! x == a[mid]

The function returns mid, which is 43.


"""
