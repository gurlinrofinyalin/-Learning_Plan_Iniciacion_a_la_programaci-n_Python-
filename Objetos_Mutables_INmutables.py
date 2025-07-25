#Objetos mutables e inmutables

# Obtener la dirección de memoria de una variable
a = 65
print("La dirección de memoria es" , id(a))#139793813071784

# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria es" ,id(miNumero))  #139793813071784
print("La dirección de memoria es" , id(miNumero2))#139793813071784
# son las mismas

# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a = 65
print("La dirección de memoria es" , id(a))#139793813071784
a+=2# sumas 2 al 65 y se cambia la direccion
print("La dirección de memoria es" , id(a))#139793813071848
print('------------------------------------------')



# Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5)# una  tupla
print("La dirección de memoria es" , id(a))#140285853072288


# Obtener la dirección de memoria de una lista
a = [1, 2, 3, 4, 5]
print("La dirección de memoria es" , id(a))#140285855267200

# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}
print(a)# {'a': 1, 'b': 2}
print("La dirección de memoria es" , id(a)) #140285855266240

# modificamos el diccionario añadiendo un elemento 3
# no se modifica la direccion del diccionario
a["c"] = 3
print(a)#{'a': 1, 'b': 2, 'c': 3}
print("La dirección de memoria es" , id(a)) #140285855266240