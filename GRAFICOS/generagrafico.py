import matplotlib.pyplot as plt
import numpy as np

# etiquetas
labels = ['Asesinatos', 'Descuartizaciones', 'Pedrastia', 'Envenenamiento', 'Bombas']
# barra de hombres
men_means = [33, 34, 40, 35, 27]
# barra de hombres
women_means = [25, 20, 34, 40, 45]


x = np.arange(len(labels))  # localizacion de las etiquetas
width = 0.30  # ancho de las barras

fig, ax = plt.subplots() # creas la figura y los ejees
"""
fig (Figura): 
Es el lienzo o la ventana completa donde se dibujará tu gráfico. 
Imagina que es el papel en blanco donde vas a pintar. 
Una figura puede contener uno o varios gráficos (ejes). 
Cuando haces fig, ax = plt.subplots(), estás creando una nueva figura (fig) 
y un conjunto de ejes (ax) dentro de ella.

ax (Ejes/Axes): 
Es el área específica dentro de la figura donde realmente se dibuja el gráfico. 
Contiene los datos, las etiquetas de los ejes, el título y cualquier elemento gráfico 
(como las barras en tu caso). 
Puedes tener varios ax dentro de una sola fig si quieres mostrar múltiples subtramas. 
En tu código, ax es donde estás dibujando las barras, estableciendo los títulos de los ejes y añadiendo las etiquetas.
"""




# leyenda  es hombres y mujeres
"""
Aquí se dibujan las barras en el gráfico.
ax.bar(...): Es la función para crear gráficos de barras.
rects1 = ax.bar(x - width/2, men_means, width, label='Hombres', color='blue'): 
Dibuja las barras para el grupo de "Hombres".
x - width/2: Posiciona cada barra de hombre ligeramente a la izquierda del centro de cada "tick" en el eje X. 
Esto es para que las barras de hombres y mujeres estén lado a lado.

men_means: Proporciona la altura de cada barra.
width: Establece el ancho de cada barra.
label='Hombres': Define la etiqueta que aparecerá en la leyenda para estas barras.
color='blue': Establece el color de las barras para los hombres en azul.

rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres', color='pink'):
Dibuja las barras para el grupo de "Mujeres".
x + width/2: Posiciona cada barra de mujer ligeramente a la derecha del centro del "tick".
women_means: Proporciona la altura de cada barra.
width: Establece el ancho de cada barra.
label='Mujeres': Define la etiqueta en la leyenda para estas barras.
color='pink': Establece el color de las barras para las mujeres en rosa.

rects1 y rects2 almacenan los objetos "Rectangle" creados, que luego se usarán para añadir 
las etiquetas de valor encima de las barras.
"""
rects1 = ax.bar(x - width/2, men_means, width, label='Hombres', color='blue')
rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres', color='pink')



ax.set_ylabel('Numero de ataques moros')# Establece la etiqueta del eje Y.

ax.set_title('Alcance por grupo y genero')# Establece el título principal del gráfico.

ax.set_xticks(x, labels)
#Establece la posición de los "ticks" (las marcas) en el eje X usando los valores de x ([0, 1, 2, 3, 4])
# y luego les asigna las etiquetas de texto correspondientes de la lista labels (['Asesinatos', ...]).



ax.legend()
#ax.legend(): Muestra la leyenda del gráfico, utilizando las label que se definieron al crear las barras
# ('Hombres' y 'Mujeres'). Esto ayuda a identificar qué barra corresponde a cada grupo.

#Estas líneas añaden las etiquetas de valor sobre las barras.
ax.bar_label(rects1, padding=3)
#Añade el valor numérico de cada barra (men_means) directamente encima de las barras de los hombres (rects1).
# padding=3 añade un pequeño espacio entre el valor y la parte superior de la barra.
ax.bar_label(rects2, padding=3)# Hace lo mismo para las barras de las mujeres (rects2).


fig.tight_layout()#Ajusta automáticamente los parámetros del subtrazado para que el gráfico quede bien espaciado y no se solapen las etiquetas ni los títulos.

plt.show()# Renderiza y muestra el gráfico en una ventana emergente. Sin esta línea, el gráfico se crearía pero no se visualizaría.

# pip install PyQt5
#debes instar este


"""
Sí, instalar PyQt5 usando pip install PyQt5 es suficiente para tener la librería en tu entorno de Python.

¿Qué es PyQt5 y por qué es relevante aquí?
PyQt5 es un conjunto de bindings de Python (esencialmente, un "enlace" o adaptador) para la librería Qt. Qt es un framework multiplataforma muy potente y popular para crear aplicaciones con interfaz gráfica de usuario (GUI).

Cuando Matplotlib necesita mostrar un gráfico de forma interactiva usando plt.show(), necesita un "backend" que sepa cómo dibujar ventanas y manejar eventos (como clics o movimientos del ratón) en tu sistema operativo. QtAgg (basado en PyQt5) y TkAgg (basado en Tkinter) son dos de los backends interactivos más comunes que Matplotlib puede usar.

Al instalar PyQt5, estás proporcionando a Matplotlib uno de los entornos gráficos que necesita para abrir esa ventana con tu gráfico cuando llamas a plt.show().


"""



"""

Explicación del Código Matplotlib para Gráficos de Barras
Aquí te detallo la función de cada sección del código:

Python

import matplotlib.pyplot as plt
import numpy as np
Estas líneas son importaciones de librerías.

import matplotlib.pyplot as plt: Importa la biblioteca Matplotlib, específicamente el módulo pyplot, que es el más utilizado para crear gráficos. Le damos el alias plt para que sea más fácil de usar en el código (en lugar de escribir matplotlib.pyplot cada vez).

import numpy as np: Importa la biblioteca NumPy, fundamental para operaciones numéricas en Python, especialmente con arreglos. Le damos el alias np. Aquí se usa para crear una secuencia de números.

Python

# etiquetas
labels = ['Asesinatos', 'Descuartizaciones', 'Pedrastia', 'Envenenamiento', 'Bombas']
# barra de hombres
men_means = [20, 34, 30, 35, 27]
# barra de hombres
women_means = [25, 32, 34, 20, 25]
Estas son las definiciones de datos.

labels: Es una lista de cadenas de texto que se usarán como las etiquetas del eje X (por ejemplo, los nombres de las categorías de ataques).

men_means: Es una lista de números que representan los valores para el grupo de "Hombres" en cada categoría. Estos serán la altura de las barras para los hombres.

women_means: Similar a men_means, esta lista de números representa los valores para el grupo de "Mujeres".

Python

x = np.arange(len(labels))  # localizacion de las etiquetas
width = 0.50  # ancho de las barras
Estas líneas configuran parámetros de posicionamiento y tamaño.

x = np.arange(len(labels)): np.arange(len(labels)) crea un arreglo NumPy con valores numéricos que van desde 0 hasta len(labels) - 1. Por ejemplo, si tienes 5 etiquetas, x será [0, 1, 2, 3, 4]. Estos números se usarán para posicionar las barras en el eje X.

width = 0.50: Define el ancho de cada barra individual. Un valor de 0.50 significa que cada barra ocupará el 50% del espacio disponible entre cada "tick" principal del eje X.

Python

fig, ax = plt.subplots()
Esta es la creación de la figura y los ejes.

fig, ax = plt.subplots(): Esta es una función de pyplot que crea una Figura (fig) y un conjunto de Ejes (ax) en un solo paso.

fig: Es el objeto Figura completo, que representa la ventana o el "lienzo" donde se dibujará todo el gráfico.

ax: Es el objeto de Ejes (Axes), que es el área real donde se trazan los datos (las barras, etiquetas, títulos de ejes, etc.). Es donde la mayoría de las operaciones de trazado se realizan.

Python

# leyenda 
rects1 = ax.bar(x - width/2, men_means, width, label='Hombres', color='blue')
rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres', color='pink')
Aquí se dibujan las barras en el gráfico.

ax.bar(...): Es la función para crear gráficos de barras.

rects1 = ax.bar(x - width/2, men_means, width, label='Hombres', color='blue'): Dibuja las barras para el grupo de "Hombres".

x - width/2: Posiciona cada barra de hombre ligeramente a la izquierda del centro de cada "tick" en el eje X. Esto es para que las barras de hombres y mujeres estén lado a lado.

men_means: Proporciona la altura de cada barra.

width: Establece el ancho de cada barra.

label='Hombres': Define la etiqueta que aparecerá en la leyenda para estas barras.

color='blue': Establece el color de las barras para los hombres en azul.

rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres', color='pink'): Dibuja las barras para el grupo de "Mujeres".

x + width/2: Posiciona cada barra de mujer ligeramente a la derecha del centro del "tick".

women_means: Proporciona la altura de cada barra.

width: Establece el ancho de cada barra.

label='Mujeres': Define la etiqueta en la leyenda para estas barras.

color='pink': Establece el color de las barras para las mujeres en rosa.

rects1 y rects2 almacenan los objetos "Rectangle" creados, que luego se usarán para añadir las etiquetas de valor encima de las barras.

Python

# Add some text for labels, title and custom x-axis tick labels, etc.
# titulo del eje Y
ax.set_ylabel('Numero de ataques moros')
# titulo del eje X
ax.set_title('Alcance por grupo y genero')
Estas líneas establecen los títulos del gráfico y los ejes.

ax.set_ylabel('Numero de ataques moros'): Establece la etiqueta del eje Y.

ax.set_title('Alcance por grupo y genero'): Establece el título principal del gráfico.

Python

ax.set_xticks(x, labels)
Esta línea configura las etiquetas del eje X.

ax.set_xticks(x, labels): Establece la posición de los "ticks" (las marcas) en el eje X usando los valores de x ([0, 1, 2, 3, 4]) y luego les asigna las etiquetas de texto correspondientes de la lista labels (['Asesinatos', ...]).

Python

ax.legend()
Esta línea muestra la leyenda.

ax.legend(): Muestra la leyenda del gráfico, utilizando las label que se definieron al crear las barras ('Hombres' y 'Mujeres'). Esto ayuda a identificar qué barra corresponde a cada grupo.

Python

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
Estas líneas añaden las etiquetas de valor sobre las barras.

ax.bar_label(rects1, padding=3): Añade el valor numérico de cada barra (men_means) directamente encima de las barras de los hombres (rects1). padding=3 añade un pequeño espacio entre el valor y la parte superior de la barra.

ax.bar_label(rects2, padding=3): Hace lo mismo para las barras de las mujeres (rects2).

Python

fig.tight_layout()
Esta línea ajusta el diseño del gráfico.

fig.tight_layout(): Ajusta automáticamente los parámetros del subtrazado para que el gráfico quede bien espaciado y no se solapen las etiquetas ni los títulos.

Python

plt.show()
Esta línea muestra el gráfico.

plt.show(): Renderiza y muestra el gráfico en una ventana emergente. Sin esta línea, el gráfico se crearía pero no se visualizaría.

En resumen, el código toma tus datos sobre ataques, los organiza por género y tipo, y luego los visualiza como un gráfico de barras comparativo, con etiquetas claras y colores distintivos para facilitar la comprensión.
"""