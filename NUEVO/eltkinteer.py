
from pathlib import Path
import sys

# Añade la ruta al sys.path
sys.path.append('/usr/lib/python3.13')

# Ahora intenta importar tkinter
import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import os
import threading
import re

# Ejemplo de uso de Path
  # Verifica si la ruta existe

# Directorio predeterminado para el archivo de salida
directorio_salida_defecto = "/home/death/Vídeos"

# Opciones de códec de audio y códec de video
opciones_acodec = ["aac", "mp3", "pcm"]
opciones_vcodec = ["libx265", "libx264", "libvpx"]


def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", initialdir="/home/death/Vídeos",
                                         filetypes=(("Archivos de vídeo mp4", "*.mp4"), ("Archivos de vídeo mkv", "*.mkv"), ("Todos los archivos", "*.*")), multiple=False)
    if archivo:
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, archivo)

        nombre_base = os.path.splitext(os.path.basename(archivo))[0]
        nombre_limpio = re.sub(r'[^a-zA-Z0-9_]', '', nombre_base)
        archivo_salida_defecto = os.path.join(directorio_salida_defecto, f'salida_{nombre_limpio}.mp4')

        entry_salida.delete(0, tk.END)
        entry_salida.insert(0, archivo_salida_defecto)


def leer_salida(proceso):
    for linea in iter(proceso.stdout.readline, ''):
        if "frame=" in linea:
            ventana.after(0, actualizar_progreso, linea)
        elif "error" in linea.lower():
            ventana.after(0, mostrar_error, linea)
    proceso.stdout.close()
    proceso.wait()


def actualizar_progreso(linea):
    try:
        frame_info = linea.split("frame=")[-1].split()[0]
        frame = int(frame_info)
        if total_frames:
            progreso_porcentaje = (frame / total_frames) * 100
            progress['value'] = progreso_porcentaje
            text_progreso.config(state="normal")
            text_progreso.insert(tk.END, f"{progreso_porcentaje:.2f}% completado\n")
        else:
            progress.step(1)
            text_progreso.config(state="normal")
            text_progreso.insert(tk.END, f"{frame} frames procesados\n")
        text_progreso.config(state="disabled")
    except ValueError:
        pass


def mostrar_error(linea):
    text_errores.config(state="normal")
    text_errores.insert(tk.END, linea, "error")
    text_errores.config(state="disabled")


def convertir_video():
    archivo_entrada = entry_archivo.get()
    archivo_salida = entry_salida.get()
    acodec = option_acodec.get()
    vcodec = option_vcodec.get()

    if archivo_entrada and archivo_salida and acodec and vcodec:
        comando = ['/usr/bin/ffmpeg', '-i', archivo_entrada, '-acodec', acodec, '-vcodec', vcodec, archivo_salida]

        # Obtener duración del video para el progreso
        comando_duracion = ['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries',
                            'stream=nb_read_frames', '-of', 'csv=p=0', archivo_entrada]
        try:
            global total_frames
            total_frames = int(subprocess.check_output(comando_duracion).strip())
            progress.config(maximum=100)  # Progreso en porcentaje
        except (subprocess.CalledProcessError, ValueError):
            total_frames = None
            progress.config(maximum=100, mode='indeterminate')  # Progreso indeterminado

        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True, bufsize=1)

        thread = threading.Thread(target=leer_salida, args=(proceso,))
        thread.start()
    else:
        print("Por favor, completa todos los campos.")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversión de video, pedrito, por un tamaño menor de tus videos")

# Crear widgets
label_archivo = tk.Label(ventana, text="Archivo de entrada:")
entry_archivo = tk.Entry(ventana, width=50)
button_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)

label_salida = tk.Label(ventana, text="Archivo de salida:")
entry_salida = tk.Entry(ventana, width=50)

label_acodec = tk.Label(ventana, text="Codec de audio:")
option_acodec = tk.StringVar(ventana)
option_acodec.set(opciones_acodec[0])
menu_acodec = tk.OptionMenu(ventana, option_acodec, *opciones_acodec)

label_vcodec = tk.Label(ventana, text="Codec de video:")
option_vcodec = tk.StringVar(ventana)
option_vcodec.set(opciones_vcodec[0])
menu_vcodec = tk.OptionMenu(ventana, option_vcodec, *opciones_vcodec)

button_convertir = tk.Button(ventana, text="Convertir", command=convertir_video)

# Barra de progreso
progress = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")

# Texto de errores
text_errores = tk.Text(ventana, height=5, width=50)
text_errores.config(state="disabled")

# Texto de progreso
text_progreso = tk.Text(ventana, height=5, width=50)
text_progreso.config(state="disabled")

# Colocar widgets en la ventana
label_archivo.grid(row=0, column=0, padx=5, pady=5)
entry_archivo.grid(row=0, column=1, padx=5, pady=5)
button_seleccionar.grid(row=0, column=2, padx=5, pady=5)

label_salida.grid(row=1, column=0, padx=5, pady=5)
entry_salida.grid(row=1, column=1, padx=5, pady=5)

label_acodec.grid(row=2, column=0, padx=5, pady=5)
menu_acodec.grid(row=2, column=1, padx=5, pady=5)

label_vcodec.grid(row=3, column=0, padx=5, pady=5)
menu_vcodec.grid(row=3, column=1, padx=5, pady=5)

button_convertir.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

progress.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

text_errores.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
text_progreso.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Iniciar bucle principal
ventana.mainloop()
