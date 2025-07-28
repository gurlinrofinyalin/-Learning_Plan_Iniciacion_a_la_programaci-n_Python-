import matplotlib


import sys
if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import filedialog, ttk
else:
    import Tkinter as tk



# Es importante colocar esta línea ANTES de importar matplotlib.pyplot
# Prueba con 'TkAgg' si tienes Tkinter instalado (generalmente viene con Python).
# Si no, y tienes PyQt5/PySide6 instalado, prueba con 'QtAgg'.
# Si ninguna de las dos funciona, puedes probar sin esta línea.
# Para instalar Tkinter (si no está): pip install tk
# Para instalar PyQt5: pip install PyQt5
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # las ubicaciones de las etiquetas
width = 0.35  # el ancho de las barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Agrega texto para etiquetas, título y etiquetas de ticks personalizados del eje x, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show() # Esta línea hará que la ventana del gráfico aparezca
#
#sudo apt-get install python3-tk