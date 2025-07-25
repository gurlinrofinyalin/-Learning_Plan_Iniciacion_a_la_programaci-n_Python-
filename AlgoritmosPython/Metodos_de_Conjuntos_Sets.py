#métodos Python tiene un conjunto de métodos integrados que puede usar en conjuntos.

"""
add() Añade un elemento al set
clear() Borra todos los elementos del set
copy() Devuelve una copia del set
difference() Devuelve un set que contiene las diferencias entre dos o más sets
difference_update() Borra los elementos del set que están incluidos en otro
discard() Borra el elemento especificado
intersection() Devuelve un set que es la intersección resultante de otros dos
intersection_update() Borra los elementos del set que no están presentes en otro
isdisjoint() Informa si dos sets tienen una intersección o no
issubset() Informa si otro set contiene a este set o no
issuperset() Informa si este set contiene a otro set o no
pop() Borra un elemento del set, no podremos elegir cuál.
remove() Borra un elemento específico
symmetric_difference() Devuelve un set con las diferencias simétricas de dos sets
symmetric_difference_update() Inserta las diferencias simétricas de este set y otro
union() Devuelve un set con la unión de dos sets
update() Actualiza el set con la unión de este set y otros
"""

# Sets iniciales para los ejemplos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2}
set_vacio = set()

print("--- Sets Iniciales ---")
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")
print(f"set_vacio: {set_vacio}\n")

# 1. add() - Añade un elemento al set
print("--- 1. add() ---")
set_para_add = {1, 2}
set_para_add.add(3)
set_para_add.add(1) # No añade si ya existe
print(f"Después de add(3): {set_para_add}\n")

# 2. clear() - Borra todos los elementos del set
print("--- 2. clear() ---")
set_para_clear = set1.copy()# hacemos una copia
set_para_clear.clear()# borramos
print(f"Después de clear(): {set_para_clear}\n")

# 3. copy() - Devuelve una copia del set
print("--- 3. copy() ---")
copia_set = set1.copy()# hacemos una copia
print(f"Copia del set1: {copia_set}")
print(f"¿Es la misma ID que set1? {set1 is copia_set}\n") # Debería ser False
# porque son distintos objetos, no se crean con =




# 4. difference() - Devuelve un set que contiene las diferencias entre dos o más sets
# (elementos en el primero que no están en los otros)
print("--- 4. difference() ---")
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
        1, 2, 3         diferencia
es como decir, cuales elementos tiene set1, que no tiene set2
a set2 le faltan 1 2 3 que si tiene set1
"""
diferencia = set1.difference(set2) #  da los elementos que no estan en set2
print(f"Elementos en set1 que no están en set2 (difference): {diferencia}\n")





# 5. difference_update() - Borra los elementos del set que están incluidos en otro
print("--- 5. difference_update() ---")
set_para_diff_update = set1.copy()
set_para_diff_update.difference_update(set2)
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
       {1, 2, 3}             difference_update
los elementos de set1 que no esten o coincidan con set2 , se salvan 
osease borro 4 y 5 que estan en los dos
y se quedan 1 2 3 del set1
"""
print(f"set_para_diff_update después de difference_update(set2): {set_para_diff_update}\n")



# 6. discard() - Borra el elemento especificado (no hace nada si no existe)
print("--- 6. discard() ---")
"""
set1 = {1, 2, 3, 4, 5}
"""
set_para_discard = set1.copy() # hacemos copia
set_para_discard.discard(3)# si existe un 3 , asique se borra
set_para_discard.discard(99) # No existe, no hay error
print(f"Después de discard(3) y discard(99): {set_para_discard}\n")
# Después de discard(3) y discard(99): {1, 2, 4, 5}






# 7. intersection() - Devuelve un set que es la intersección resultante de otros dos
print("--- 7. intersection() ---")
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
                {4, 5}             interseccion
que elementos tienen los dos     
"""
interseccion = set1.intersection(set2)
print(f"Intersección de set1 y set2: {interseccion}\n")
#Intersección de set1 y set2: {4, 5}




# 8. intersection_update() - Borra los elementos del set que no están presentes en otro
print("--- 8. intersection_update() ---")
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
                 4, 5                 intersection_update
seria como borrar los elementos en set1 que no estan en set2
se borran 1,2,3 que no estan en set2
"""
set_para_inter_update = set1.copy() # hacemos copia
set_para_inter_update.intersection_update(set2)
print(f"set_para_inter_update después de intersection_update(set2): {set_para_inter_update}\n")
# set_para_inter_update después de intersection_update(set2): {4, 5}





# 9. isdisjoint() - Informa si dos sets tienen una intersección o no
# (True si NO tienen elementos en común)
print("--- 9. isdisjoint() ---")
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
                 4, 5           False, si tienen elementos en comun 4 y 5
"""
print(f"¿set1 y set2 son disjuntos? {set1.isdisjoint(set2)}") # False (tienen 4 y 5)
print(f"¿set1 y {{9, 10}} son disjuntos? {set1.isdisjoint({9, 10})}\n") # True
#¿set1 y set2 son disjuntos? False   si tienen el 4 y el 5 en comun
#¿set1 y {9, 10} son disjuntos? True   No tienen elemenos en comun




# 12. pop() - Borra un elemento del set, NO PODREMOS ELIGIR CUAL BORRA
print("--- 12. pop() ---")
set_para_pop = {10, 20, 30}
elemento_pop = set_para_pop.pop()
print(f"Elemento eliminado con pop(): {elemento_pop}")
print(f"Set después de pop(): {set_para_pop}\n")




# 13. remove() - Borra un elemento específico (lanza KeyError si no existe)
# SE  PUEDE ELEGIR CUAL BORRAR

print("--- 13. remove() ---")
set_para_remove = set1.copy()
# NO ESTAN INDEXADOS ,  el  numero de 2  , es el valor del elemento no el indice
set_para_remove.remove(2)
# set_para_remove.remove(99) # Esto lanzaría un KeyError
print(f"Después de remove(2): {set_para_remove}\n")




# 14. symmetric_difference() - Devuelve un set con las diferencias simétricas de dos sets
# (elementos que están en uno o en otro, pero no en ambos)
print("--- 14. symmetric_difference() ---")
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
        1, 2, 3        6, 7 ,8      symmetric_difference
cuales elementos no coinciden en los dos sets 
naturalmente  1 2 3 6 7 8
"""
diferencia_simetrica = set1.symmetric_difference(set2)
print(f"Diferencia simétrica de set1 y set2: {diferencia_simetrica}\n")
#Diferencia simétrica de set1 y set2: {1, 2, 3, 6, 7, 8}




# 15. symmetric_difference_update() - Inserta las diferencias simétricas de este set y otro
print("--- 15. symmetric_difference_update() ---")
set_para_sym_diff_update = set1.copy()
set_para_sym_diff_update.symmetric_difference_update(set2)
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
        1, 2, 3        6, 7 ,8      symmetric_difference_update
se actualiza el set1  con los  elementos que no coinciden en los dos sets
naturalmente  1 2 3 6 7 8   no coinciden
y se quitan los elementos que coinciden en los dos sets  osease 4 y 5 

"""
print(f"set_para_sym_diff_update después de symmetric_difference_update(set2): {set_para_sym_diff_update}\n")
#set_para_sym_diff_update después de symmetric_difference_update(set2): {1, 2, 3, 6, 7, 8}


# 16. union() - Devuelve un set con la unión de dos sets
print("--- 16. union() ---")
union_sets = set1.union(set2)
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
        1, 2, 3, 4, 5, 6, 7, 8   union  SIN repeticion en NUEVO SET
"""
print(f"Unión de set1 y set2: {union_sets}\n")
#Unión de set1 y set2: {1, 2, 3, 4, 5, 6, 7, 8}



# 17. update() - Actualiza el set con la unión de este set y otros
print("--- 17. update() ---")
set_para_update = set1.copy()
"""
set1 = {1, 2, 3, 4, 5}
set2 =          {4, 5, 6, 7, 8}
        1, 2, 3, 4, 5, 6, 7, 8   union  SIN repeticion en set1
"""
set_para_update.update(set2)
print(f"set_para_update después de update(set2): {set_para_update}\n")






print("\n--- Relación Directa de issubset() y issuperset() ---")
set_pequeno = {1, 2}
set_grande =  {1, 2, 3, 4}
set_sin_relacion =         {5, 6}
###########
# Caso donde set_pequeno ES un subconjunto de set_grande
print(f"\n set_pequeno: {set_pequeno}, set_grande: {set_grande}")

# el set pequeño esta  contenido en el set grande
print(f"¿set_pequeno.issubset(set_grande)? {set_pequeno.issubset(set_grande)}")       # True

# el set grande contiene el set pequeño
print(f"¿set_grande.issuperset(set_pequeno)? {set_grande.issuperset(set_pequeno)}") # True (¡son consistentes!)


###########
# Caso donde set_pequeno NO ES un subconjunto de set_sin_relacion
print(f"\n set_pequeno: {set_pequeno}, set_sin_relacion: {set_sin_relacion}")

# el set pequeño esta  contenido en el set grande
print(f"¿set_pequeno.issubset(set_sin_relacion)? {set_pequeno.issubset(set_sin_relacion)}") # False

# el set grande contiene el set pequeño
print(f"¿set_sin_relacion.issuperset(set_pequeno)? {set_sin_relacion.issuperset(set_pequeno)}") # False (¡son consistentes!)


