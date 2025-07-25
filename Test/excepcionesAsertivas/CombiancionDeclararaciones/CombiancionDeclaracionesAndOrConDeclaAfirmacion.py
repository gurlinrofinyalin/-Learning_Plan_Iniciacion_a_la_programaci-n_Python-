#Combinación de varias declaraciones and/or con declaraciones de afirmación
"""
También es posible combinar múltiples condiciones
con OR o AND y probar los comandos encadenados
con la declaración de afirmación:
"""
true_statement = 5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2
print(true_statement, false_statement)#True False
assert true_statement # Success Example
try:
    assert false_statement # Fail Example
except AssertionError:
        print("AssertionError 1")

true_or_statement = 5 == 5 or 3 == 3
false_or_statement = 7 == 3 or 10 == 1
print(true_or_statement, false_or_statement)#True False
assert true_or_statement # Success Example
try:
    assert false_or_statement # Fail Example
except AssertionError:
    print("AssertionError 2")
