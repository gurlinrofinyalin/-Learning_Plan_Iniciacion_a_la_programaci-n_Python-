G = 'Esta variable es de ámbito Global'
def f1():
    E = 'Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'Esta variable es local a f2'
        E = 'E tambien es local a f2'
        G='G tambien es local a f2 '
        print(L, E, G, sep= '\n')
        f2()

    def f3():
        print(L)  #error
        f2()
        f3()
f1()

"""
 Esta vez, cuando intentamos acceder a una variable
local a f2 desde f3, nos salta un error de nombre.
"""