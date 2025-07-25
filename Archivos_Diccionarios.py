
"""
¿Cómo haríamos si quisiéramos guardar este
diccionario en un archivo y posteriormente abrirlo
siempre que queramos consultarlo?

Para ello usamos el paquete Path y Pickle
(los veremos más detalladamente en otro momento).

Pickle nos ofrece procedimientos para poder leer y escribir diccionarios
en archivos.

El paquete Path lo utilizamos para comprobar si el archivo existe.

Veamos un ejemplo sencillo para leer un archivo y guardarlo en un diccionario:
"""
import pickle# importar modulo




# escribir el diccionario en un archivo
mydict2 = {'1111111': 18, '22222222': 19, '33333333': 20}
output2 = open('archivos/myfile2.pkl', 'wb')
pickle.dump(mydict2, output2)
output2.close()

# leemos  el diccinario en el archivo
pkl_file3 = open('archivos/myfile2.pkl','rb')
mydict3 = pickle.load(pkl_file3)
print(mydict3)
pkl_file3.close()




print('-------------------')
import pickle
from pathlib import Path

d = dict()# crear un diccionario vacio

#Solicitar el nombre del archivo desde el que cargar el diccionario
# Ask for file name to load dictionary from
file_name = input("Introduce el nombre del archivo con los datos: ")
# debes poner  myfile2.pkl
#Comprobamos que existe el archivo
path = Path(f"./archivos/{file_name}")


# segurar que el directorio 'archivos' existe (¡NUEVO!)
path.parent.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe
print(path)
if path.is_file():
    # Abrir archivo en modo lectura Open file in reading mode
    input_file = open (path, 'rb')# cambio file_name por path
    d = pickle.load(input_file)
    print(f" leemos el diccionario {d}")
    # cierra el archivo Close de file
    input_file.close()
else:
    print(f"Creando archivo vacío: {path}")
    d = {}  # Diccionario vacío si el archivo no existe
    # Abrir, guardar y cerrar explícitamente
    output_file = open(path, 'wb')  # Modo escritura binaria
    try:
        pickle.dump(d, output_file)  # Guardar diccionario vacío
    finally:
        output_file.close()  # Asegurar que se cierra incluso si hay error



##Verifique los valores o agregue nuevos Check for values or add new ones
document_number = input("Introduce un documento de indentidad ")
if document_number in d:
    # #Comprueba si está en dict o no Check whether it is on dict or not
    print("La edad de" + document_number + " es " + str(d[document_number]))
else:
    age = input("Documento no existente. Introduce edad: ")
    if age.isnumeric():
        num = int(age)
        d[document_number] = num
        print("Añadido al diccionario")

#Guardar el diccionario en el archivo y cerrarlo Save dict on file and close
output_file = open(path,'wb')
pickle.dump(d, output_file)
output_file.close()