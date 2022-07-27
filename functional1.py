def square(n):
    return n*n

def increment(n):
    return n+1

"""
En la función apply el primer argumento es una lista
de funciones. El procedimiento de la función es aplicar
estas funciones al argumento y retornar el resultado.
Para ello en el RETURN, usamos la primeración a aplicar
y recursivamente volvemos a llamar a la función apply
solo que apartir del segundo elemento (segunda función 
a aplicar) en adelante.
"""
def apply(opList, arg):
    if len(opList) == 0:
        return arg
    else:
        return apply(opList[1:], opList[0](arg))

"""
Nuestro primer argumento será una lista de listas,
Es decir, cada lista interior será una secuencia de operaciones
o funciones. Nuestro segundo argumento será una lista de 
las posibles siguientes funciones (solo tenemos 2 en nuestro caso)
"""
def addLevel(opList, fctList):
    return [x + [y] for y in fctList for x in opList]

def findSequence(initial, goal):
    opList = [[]]
    """
    creamos un bucle de 'goal - initial +1' pasos, ya que
    es lo máximo que podría haber si solo hacemos INCREMENT 
    (ya que talvez ese era el procedmiento con el mínimo de pasos)
    """
    for i in range(1, goal-initial+1):
        opList = addLevel(opList, [increment, square])
        for seq in opList:
            if apply(seq, initial) == goal:
                return seq

answer = findSequence(1,100)
print(f"answer : {answer}")

# if __name__ == "__main__":
#     print(apply([], 7)) # 7
#     print(apply([increment], 7)) # 7+1 = 8
#     print(apply([increment, square], 7)) # (7+1)^2=64

#     print(addLevel([[increment]], [increment, square]))
#     # [[<function increment at 0x000001948AA99430>, <function increment at 0x000001948AA99430>], [<function increment at 0x000001948AA99430>, <function square at 0x000001948A1DEF70>]]




