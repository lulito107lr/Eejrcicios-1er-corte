from pulp import LpVariable, LpProblem, LpMinimize, value

def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    det = 0
    for c in range(n):
        submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
        signo = (-1) ** c
        det += signo * matriz[0][c] * determinante(submatriz)
    return det

def transpuesta(matriz):
    n = len(matriz)
    return [[matriz[j][i] for j in range(n)] for i in range(n)]

# Definimos variables PuLP
a11 = LpVariable("a11", cat="Continuous")
a12 = LpVariable("a12", cat="Continuous")
a13 = LpVariable("a13", cat="Continuous")
a21 = LpVariable("a21", cat="Continuous")
a22 = LpVariable("a22", cat="Continuous")
a23 = LpVariable("a23", cat="Continuous")
a31 = LpVariable("a31", cat="Continuous")
a32 = LpVariable("a32", cat="Continuous")
a33 = LpVariable("a33", cat="Continuous")

# Asignamos valores arbitrarios
prob = LpProblem("Determinante", LpMinimize)
prob += 0

a11.setInitialValue(6)
a12.setInitialValue(2)
a13.setInitialValue(8)
a21.setInitialValue(3)
a22.setInitialValue(7)
a23.setInitialValue(1)
a31.setInitialValue(4)
a32.setInitialValue(9)
a33.setInitialValue(5)

# Construimos la matriz original
matriz_original = [
    [value(a11), value(a12), value(a13)],
    [value(a21), value(a22), value(a23)],
    [value(a31), value(a32), value(a33)]
]

# Calculamos determinante original
det_original = determinante(matriz_original)

# Calculamos determinante de la transpuesta
matriz_transpuesta = transpuesta(matriz_original)
det_transpuesta = determinante(matriz_transpuesta)

# Mostramos resultados
print("Determinante de la matriz original:", det_original)
print("Determinante de la transpuesta:", det_transpuesta)
