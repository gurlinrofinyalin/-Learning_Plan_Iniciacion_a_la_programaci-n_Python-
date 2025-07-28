import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

# pip install PyQt5
#debes instar este


"""
Sí, instalar PyQt5 usando pip install PyQt5 es suficiente para tener la librería en tu entorno de Python.

¿Qué es PyQt5 y por qué es relevante aquí?
PyQt5 es un conjunto de bindings de Python (esencialmente, un "enlace" o adaptador) para la librería Qt. Qt es un framework multiplataforma muy potente y popular para crear aplicaciones con interfaz gráfica de usuario (GUI).

Cuando Matplotlib necesita mostrar un gráfico de forma interactiva usando plt.show(), necesita un "backend" que sepa cómo dibujar ventanas y manejar eventos (como clics o movimientos del ratón) en tu sistema operativo. QtAgg (basado en PyQt5) y TkAgg (basado en Tkinter) son dos de los backends interactivos más comunes que Matplotlib puede usar.

Al instalar PyQt5, estás proporcionando a Matplotlib uno de los entornos gráficos que necesita para abrir esa ventana con tu gráfico cuando llamas a plt.show().


"""