"""

Comparación de la
eficiencia de los
algoritmos
Considerando, una vez más, que tenemos 85.000
alumnos y que en cada iteración de búsqueda se
descarta la mitad de la lista que no es la que
buscamos, podemos calcular mediante logaritmos en
base 2 y concluir que con cada petición del función
de búsqueda, en el peor de los casos, se realizan
operaciones lg(N), es decir,
lg(85000) ≃ 16 operaciones.
Pero aún no ha terminado, ya que hicimos 3500
llamadas a esta función, por lo que realizamos (3500
* 16) ≃ 56000 operaciones.
Así, pudimos optimizar nuestro algoritmo que antes
realizaba casi 300 millones de operaciones a solo 56
mil.
Una vez más hemos comprobado la importancia de
pensar en cómo se comportarán nuestros algoritmos
de acuerdo a la cantidad de datos recibidos, y vale la
pena recalcar que aunque existan abstracciones de
tales funciones, como la función index() que
realizaría esta búsqueda con solo una llamada, es
muy importante aprender estos fundamentos.
Importante recalcar que para la solución de
búsqueda binaria es necesario tener la lista
ordenada, por lo que usamos la función sorted() para
ordenarla.

"""