from pulp import LpVariable, LpProblem, LpMinimize, value

# Función recursiva para calcular el determinante de una matriz cuadrada
def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    det = 0
    for c in range(n):
        # Submatriz sin la primera fila y la columna c
        submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
        signo = (-1) ** c
        det += signo * matriz[0][c] * determinante(submatriz)
    return det

# Definimos variables PuLP para una matriz 3x3
a11 = LpVariable("a11", cat="Continuous")
a12 = LpVariable("a12", cat="Continuous")
a13 = LpVariable("a13", cat="Continuous")
a21 = LpVariable("a21", cat="Continuous")
a22 = LpVariable("a22", cat="Continuous")
a23 = LpVariable("a23", cat="Continuous")
a31 = LpVariable("a31", cat="Continuous")
a32 = LpVariable("a32", cat="Continuous")
a33 = LpVariable("a33", cat="Continuous")

# Creamos un problema vacío para inicializar valores
prob = LpProblem("Determinante", LpMinimize)
prob += 0

# Asignamos valores arbitrarios
a11.setInitialValue(7)
a12.setInitialValue(15)
a13.setInitialValue(0)
a21.setInitialValue(8)
a22.setInitialValue(6)
a23.setInitialValue(0)
a31.setInitialValue(2)
a32.setInitialValue(11)
a33.setInitialValue(0)

# Construimos la matriz con los valores
matriz = [
    [value(a11), value(a12), value(a13)],
    [value(a21), value(a22), value(a23)],
    [value(a31), value(a32), value(a33)]
]

# Imprimimos el determinante
print("Determinante:", determinante(matriz))
