
#Acceso a elementos de la lista
"""
indexing
slicing
stride

"""
# indexing
lista=["texto1","texto2","texto3","texto4","texto5"]
print(lista[0])# primer elemento #texto1
print(lista[-1])#ultimo elemento #texto5

# slicing
print(lista[2:4])#['texto3', 'texto4']
print(lista[:3])#['texto1', 'texto2', 'texto3']
print(lista[2:])#['texto3', 'texto4', 'texto5']


# stride
# salta de 3 elementos en 3 elementos
# ademas el elemento final como el 4,no cuenta
print(lista[0:4:3])#['texto1', 'texto4']


# darle la  vuelta a una lista con el stride
print(lista)#['texto1', 'texto2', 'texto3', 'texto4', 'texto5']
print(lista[::-1])#['texto5', 'texto4', 'texto3', 'texto2', 'texto1']

# cambio entre los strings y las listas
# construcciones sintacticas indexacion  [:]

# cuando lo usamos con un string , nos devuelve una referencia a ese mismo objeto
texto = "Hola mundo"
print(texto[:])#Hola mundo
# comprobacion de que son el mismo objeto
print(texto[:] is texto)# True


# cuando usamos una listam nos devuelve una copia del objeto
lista = [1,2,3,4]
print(lista[:])#[1, 2, 3, 4]
# comprobacion de que NO SON EL MISMO OBJETO
print(lista[:] is lista)# False


