dic1 = {
"key1": "value1",
"key2": "value2"
}
dic2 = {
"key3": "value3",
"key4": "value4"
}
# son el mismo objeto
print(dic1 is  dic2)#False

# son el mismo objeto
print(dic1 == dic2)#False


# son el mismo objeto
print(dic1 is  dic1)#True

# son el mismo objeto
print(dic1 == dic1)#True

try:
    dic1 + dic2
except TypeError:
    print("no se puede unir  diccionarios asi")


#Quitar valores de diccionario
#Diccionario.pop("edad")#Quitaría La pareja edad:43

#Meter un diccionario dentro de otro diccionario:
miDiccionario={"nombre": "Jordan",
               "Equipo": "Bulls",
                "Anillos": {"Temporadas": [1991, 1992, 1993, 1996, 1997, 1998]},
               "Pais":"Francia"}
print(miDiccionario)# {'nombre': 'Jordan', 'Equipo': 'Bulls', 'Anillos': {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}, 'Pais': 'Francia'}

print(miDiccionario.keys())#Me imprime Las claves
# dict_keys(['nombre', 'Equipo', 'Anillos', 'Pais'])

print(miDiccionario.values())#Me imprime el valor de Las claves
#dict_values(['Jordan', 'Bulls', {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}, 'Francia'])

print(len(miDiccionario))#Imprime La Longitud del diccionario 4

print(miDiccionario["Pais"])#Búsqueda clave, devuelve valor Francia
print(miDiccionario)#Imprimo el diccionario entero.
# {'nombre': 'Jordan', 'Equipo': 'Bulls', 'Anillos': {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}, 'Pais': 'Francia'}


#Crear un diccionario a partir de dos listas
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario=dict(zip(lista_claves, lista_valores))
print(diccionario)#{'nombre': 'Angel', 'edad': 43}
print(type(diccionario))#<class 'dict'>
print(diccionario["nombre"])#Angel

# nos devuelve un tipo zip, hay que convertirlo a lista
Lista=list(zip(lista_claves, lista_valores))
print(Lista)#[('nombre', 'Angel'), ('edad', 43)]
print(type(Lista))#<class 'list'>
print(Lista[0])#('nombre', 'Angel')
print(Lista[0][1])# Angel


#Comprobar si una clave está en el diccionario
print("nombre" in diccionario)#True      Devuelve true o false

print("@"*30)

# Crear un diccionario
#Partiendo de un dicconario vacío y añadiendo campos uono a uno
miDiccionario = {}
miDiccionario["nombre"] = "Ana"
miDiccionario["edad"] = 9
miDiccionario["grupo"] = "4 primaria"
print(miDiccionario)#{'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria'}

#Utilizando la función dict()
# Las claves son parámetros de la función dict()
miDiccionario = dict(nombre="Ana",
                     edad=9,
                     grupo="4 primaria",
                     nota="Sobresaliente")

print(miDiccionario)#{'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria', 'nota': 'Sobresaliente'}

# AL CREAR UN TIPO zip nos devuelve un objeto tipo ZIP


#Uniendo Listas de claves-valores con la función zip()
claves=["nombre","edad","grupo","nota"]
valores = ["Ana", 9, "4 primaria","Sobresaliente"]
miDiccionario = dict(zip(claves, valores))
print(miDiccionario) #{'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria', 'nota': 'Sobresaliente'}
print(miDiccionario["nombre"])# Ana
print(type(miDiccionario["nombre"]))# <class 'str'>

# Uniendo Listas de claves-valores con la función zip()
# este objeto zip  tenemos que covertirlo a zip
claves = ["nombre", "edad", "grupo", "nota"]
valores = ["Ana", 9, "4 primaria", "Sobresaliente"]
Lista = list(zip(claves, valores)) # lista de tuplas
print(Lista)  # [('nombre', 'Ana'), ('edad', 9), ('grupo', '4 primaria'), ('nota', 'Sobresaliente')]
print(Lista[0][1])#Ana
print(type(Lista[0]))#<class 'tuple'>




d = {'edad': 10,
 'grupo': '4 Primaria',
 'apellidos': ['Garcia','Fernandez'],
 'nombre': 'Beatriz',
 'notas': {'música': 'excelente',
           'lengua': 'notable',
           'matematicas': 'excelente'}
     }

#Anidamiento en diccionarios
d['notas']['ingles'] = 'notable' # Crea nueva entrada en dict anidado

print(d)
#{'edad': 10, 'grupo': '4 Primaria', 'apellidos': ['Garcia', 'Fernandez'], 'nombre': 'Beatriz', 'notas': {'música': 'excelente', 'lengua': 'notable', 'matematicas': 'excelente', 'ingles': 'notable'}}

d={'nombre': 'Beatriz',
   'apellidos': ['García', 'Fernandez'],
   'edad': 10,
   'grupo': '4 Primaria',
   'notas': {'matematicas': 'excelente',
             'lengua':'notable',
             'música': 'excelente'}
   }


print(d)
#{'nombre': 'Beatriz', 'apellidos': ['García', 'Fernandez'], 'edad': 10, 'grupo': '4 Primaria', 'notas': {'matematicas': 'excelente', 'lengua': 'notable', 'música': 'excelente'}}

print(d['nombre'])#Beatriz

print(d['notas']['música'])#excelente   # Acceso al diccionario anidado

print(d['apellidos'][0])# García      # Acceso al ler elem. de la lista anidada



#En los diccionarios no se acceden utilizando un índice
#si no a través del nombre de la clave entre corchetes
x = thisdict = {'model': "scoda", '22222222': 19, '33333333': 20}
x = thisdict["model"]
print(x)# scoda


#Método get()
dic2 = {
    0: "cero",1: "uno",
    2: "dos",3: "tres"
}

print(dic2[0])#cero
print(dic2[3])#tres


# se peude usar cualquier objeto inmutable , para la clave de un diccionario
# numeros string tuplas entre otros
dic3 = {
    ("uno", 1): "one",
    ("dos", 2): "two",
    ("tres",3): "three"
}
# la clave es una tupla
print(dic3["uno", 1])#one
print(dic3["dos", 2])#two


thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# cambiar el año
thisdict["year"] = 2018

#Recorrer un diccionario
# el valor de retorno son las claves del diccionaerio
for x in thisdict:
    print (x)
    # brand
    # model
    # year

# imprimir todos los valores
for x in thisdict:
    print(thisdict[x])
    #Ford
    #Mustang
    #2018


# Función values() devolver valores en un diccionario
for x in thisdict.values():
    print (x)
    #Ford
    # Mustang
    # 2018

#Función items()  devuelve la clave y el valor con el iterador
for x, y in thisdict.items():
    print (x, y)
    # brand Ford
    # model Mustang
    # year 2018


#Comprobar si existe una clave en un diccionario  Palabra clave in
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# cuantos elemetnos de clave y valor , hay en el diccinario
print(len(thisdict))#3


#Agregar elementos
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


#Eliminar elementos pop
# eliminar con el nombre de la clave
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict)#('brand': 'Ford', 'year': 1964}


# version anteriores a 3.7 SE ELIMINA UN ELEMENTO DE MANERA ALEATORIA
# con la versiion de 3.7 se elinna el ultimo

#Método popitem()
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)#('brand': 'Ford', 'model': 'Mustang'}



# eliminar el elemento con la Palabra clave del y el nombre especificado
# ya no es el ultimo
thisdict = {
"brand":"Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)#('brand': 'Ford', 'year': 1964}
# Provoca un error de tupoo NameError si quieres borrar algo que
# ya no existe o quieres acceder a el
thisdict = {
"brand":"Ford",
"model": "Mustang",
"year": 1964
}
del thisdict
try:
    print(thisdict)
except NameError:
    print("no se puede acceder a el diccionario se borro")



# borrar  los elementos del diccionario con clear
thisdict = {
"brand":"Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)#{}


# COPIAR UN  DICCIONARIO NO SE PUEDE HACER ASI
dic2 = dic1
# porque dic2 seria una referencia a dic1
# los cambios realizados en dic1 se realizan auto en dic2
# si cambias algo en dic1

thisdict = {
"brand":"Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# hacer una copia de un diccionario con dict
thisdict = {
"brand":"Ford",
"model": "Mustang",
"year": 1964
}
mydict = dict(thisdict)
print(mydict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# diccionarios anidados
myfamily = {
    "child1" : {
        "name":"Emil",
        "year" : 2004
    },
    "child2" : {
        "name":"Tobias",
        "year" : 2007
    },
    "child3" : {
        "name":"Linus",
        "year": 2011
    }
}

child1= {
    "name": "Emil",
    "year": 2004
}
child2= {
    "name": "Tobias",
    "year": 2007
}
child3= {
    "name": "Linus",
    "year": 2011
}
# diccionario que contien los 3 diccionarios
myfamily = {
"childl" : child1,
"child2" : child2,
"child3" : child3
}



#Constructor dict()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}




#https://apps.skillsbuild.skillsnetwork.site/learning/course/course-v1:BeJob+sNABLy+v1/block-v1:BeJob+sNABLy+v1+type@sequential+block@7aa805a0596b4582a86299ffc6cf59ee/block-v1:BeJob+sNABLy+v1+type@vertical+block@f5c6fa7d1a72465ba57e4f0cf3817912


