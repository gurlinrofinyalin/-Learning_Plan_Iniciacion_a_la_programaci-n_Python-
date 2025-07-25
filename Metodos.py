
# MÉTODOS DE LOS STRINGS:
# lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower())
#este texto está inicialmente en mayúsculas


# capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize())
#Este texto no tenía la primera letra en mayúsculas


# count(): Cuenta cuantas veces aparece una letra o una cadena
# de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3.count('c'))
#4   el numero de veces que sale c en la frase

# find(): Representa el índice o la posición en el cual
# aparece un carácter o un grupo de caracteres.
# Si aparece varias veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4.find('e'))
#9    en el caracter con indice 9 sale una e por primera vez
print(s_texto4[9])# e   los string son arrays


#Representa el índice o la posición en el cual
# aparece un carácter o un grupo de caracteres.
# Si aparece varias veces me dice sólo el primero.
# rfind(): Igual que find() pero contando desde atrás.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5.rfind('desde'))


# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un
#string. Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"#
print(s_texto6.isdigit())# ¿es un string ? True , si es un string

print("4".isdigit())# True , m si es un  string
print(s_texto6.isdigit())# ¿es un string ? True , si es un string

# isalum(): Devuelve un boolean, Devuelve verdadero si todos los
#caracteres de la cadena son numéricos y hay al menos un carácter.
#En caso contrario, devuelve falso.
s_texto7 = "9857654gf7"
print(s_texto7.isalnum())# son todos los caracteres numericicos False

# isalpha(): Devuelve un boolean, comprueba si hay sólo letras.
#Los espacios no cuentan.
s_texto8 = "Holamundo"
print(s_texto8.isalpha()) # hay solo letras True


# split(): Separa por palabras utilizando espacios.
# osease separa el string  cuando encuentra un espacio
# #Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())
#['Vamos', 'a', 'separar', 'esta', 'frase', 'por', 'los', 'espacios']


# Podemos usar otro carácter como separador, por ejemplo una coma:
# osease separa el string por la coma
# crea una lista
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print(s_texto10.split(","))
# ['Esta sería la primera parte', 'y esta la segunda']


# strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = " En este texto había espacios al principio y al final "
print(s_texto11.strip())
#   "En este texto había espacios al principio y al final"


# replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
# reemplazamos la palabra casa por la palabra hogar
print(s_texto12.replace("casa", "hogar"))
#Vamos reemplazar la palabra hogar



# Te invito a que inspecciones el resto de funciones predefinidas para los strings en:
# https://www.freecodecamp.org/espanol/news/metodos-de-string-de-pythonexplicados-con-ejemplo/



# isnumeric si es un numero
l = list() #Creamos una lista vacia

texto = input("Introduce un número entero por teclado: ")
if texto.isnumeric():  # Comprobamos si son numeros
    #  pregunta si es un numero  , si lo  es un numero hacemos casting
    num = int(texto)# casteamos a entero
    l.append(num) # agregamos a la lista
    print ("Número " + str(num) + " añadido a la lista")
else:
    print("No has introducido un número entero")




# join
import random
letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random.shuffle(letras)  # baraja las letras

print(letras)  #
['y', 'x', 'j', 'i', 'b', 'm', 'n', 'k', 'r', 'v', 'g', 'a', 'f', 'u', 'e', 'w', 'p', 't', 'q', 'd', 'h', 'z', 'l',
 'o', 'c', 's']

print(''.join(letras))  # junta los elementos de la lista
# usa el espacio
# rqkmjgvzblsaoicfntxewduphy




# upper
# recorremos el string que es un array , lo ponemos en mayuscula
for letra in 'Python':
    print(letra.upper(), end=' ')
#P Y T H O N
print("\n---------")
