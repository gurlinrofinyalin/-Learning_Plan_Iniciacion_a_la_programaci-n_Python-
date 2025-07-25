import pickle
from pathlib import Path

# Escribir diccionario en archivo (ejemplo inicial)
mydict2 = {'1111111': 18, '22222222': 19, '33333333': 20}
with open('archivos/myfile2.pkl', 'wb') as output2:
    pickle.dump(mydict2, output2)

# Leer diccionario desde archivo
with open('archivos/myfile2.pkl', 'rb') as pkl_file3:
    mydict3 = pickle.load(pkl_file3)
print(mydict3)

print('-------------------')

# Crear diccionario vacío
d = dict()

# Solicitar nombre del archivo
file_name = input("Introduce el nombre del archivo con los datos: ")
path = Path(f"./archivos/{file_name}")

# Asegurar que el directorio existe
path.parent.mkdir(parents=True, exist_ok=True)

# Cargar o crear archivo
if path.is_file():
    with open(path, 'rb') as input_file:
        d = pickle.load(input_file)
    print(f"Leemos el diccionario: {d}")
else:
    print(f"Creando archivo vacío: {path}")
    d = {}
    with open(path, 'wb') as output_file:
        pickle.dump(d, output_file)

# Interactuar con el diccionario
document_number = input("Introduce un documento de identidad: ")
if document_number in d:
    print(f"La edad de {document_number} es {d[document_number]}")
else:
    age = input("Documento no existente. Introduce edad: ")
    if age.isnumeric():
        d[document_number] = int(age)
        print("Añadido al diccionario")

# Guardar cambios
with open(path, 'wb') as output_file:
    pickle.dump(d, output_file)
print("Diccionario guardado correctamente")