# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector',
     'Apellidos':'Costa Guzman',
     'dni':'11111111A'},
    {'Nombre': 'Juan',
     'Apellidos':'González Márquez',
     'dni':'22222222B'}
]
print(type(clientes))# <class 'list'>  una lista de diccionarios
# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        # c['dni'] c diccionario dni clave
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return

    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        # i indice   c  <class 'dict'>
        print(f" {i}  {c}  {type(c)}")
        """
         0  {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}
         1  {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}
        """
        if (dni == c['dni']):
            # clientes lista de diccionarios   i indice
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return
    print('Cliente no encontrado')

### Fíjate muy bien cómo se utiliza el código estructurado
print("==LISTADO DE CLIENTES==")
print(clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '11111111Z')
print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')
print("\n==LISTADO DE CLIENTES==")
print(clientes)



"""
==LISTADO DE CLIENTES==
[{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}, {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}]

==MOSTRAR CLIENTES POR DNI==
Hector Costa Guzman
Cliente no encontrado

==BORRAR CLIENTES POR DNI==
Cliente no encontrado
{'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'} > BORRADO

==LISTADO DE CLIENTES==
[{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}]
"""


"""
==LISTADO DE CLIENTES==
[{'Nombre': 'Hector', 'Apellidos':
'Costa Guzman', 'dni': '11111111A'},
{'Nombre': 'Juan', 'Apellidos':
'González Márquez', 'dni': '22222222B'}]
==MOSTRAR CLIENTES POR DNI==
Hector Costa Guzman
Cliente no encontrado
==BORRAR CLIENTES POR DNI==
Cliente no encontrado
{'Nombre': 'Juan', 'Apellidos':
'González Márquez', 'dni': '22222222B'}
> BORRADO
==LISTADO DE CLIENTES==
[{'Nombre': 'Hector', 'Apellidos':
'Costa Guzman', 'dni': '11111111A'}]"""