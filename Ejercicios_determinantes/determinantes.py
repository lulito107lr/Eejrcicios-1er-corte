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
        # Construimos la submatriz excluyendo la primera fila y la columna c
        submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
        signo = (-1) ** c
        det += signo * matriz[0][c] * determinante(submatriz)
    return det

# Creamos variables PuLP para una matriz 4x4
a11 = LpVariable("a11", cat="Continuous")
a12 = LpVariable("a12", cat="Continuous")
a13 = LpVariable("a13", cat="Continuous")
a14 = LpVariable("a14", cat="Continuous")
a21 = LpVariable("a21", cat="Continuous")
a22 = LpVariable("a22", cat="Continuous")
a23 = LpVariable("a23", cat="Continuous")
a24 = LpVariable("a24", cat="Continuous")
a31 = LpVariable("a31", cat="Continuous")
a32 = LpVariable("a32", cat="Continuous")
a33 = LpVariable("a33", cat="Continuous")
a34 = LpVariable("a34", cat="Continuous")
a41 = LpVariable("a41", cat="Continuous")
a42 = LpVariable("a42", cat="Continuous")
a43 = LpVariable("a43", cat="Continuous")
a44 = LpVariable("a44", cat="Continuous")

# Creamos un problema vacío para inicializar valores
prob = LpProblem("Determinante_4x4", LpMinimize)
prob += 0  # No hay función objetivo, solo usamos PuLP para definir variables

# Asignamos valores arbitrarios a cada variable
a11.setInitialValue(4)
a12.setInitialValue(14)
a13.setInitialValue(1)
a14.setInitialValue(6)
a21.setInitialValue(-10)
a22.setInitialValue(-19)
a23.setInitialValue(17)
a24.setInitialValue(-3)
a31.setInitialValue(-8)
a32.setInitialValue(16)
a33.setInitialValue(-15)
a34.setInitialValue(11)
a41.setInitialValue(2)
a42.setInitialValue(-12)
a43.setInitialValue(0)
a44.setInitialValue(7)

# Construimos la matriz con los valores extraídos de las variables
matriz_4x4 = [
    [value(a11), value(a12), value(a13), value(a14)],
    [value(a21), value(a22), value(a23), value(a24)],
    [value(a31), value(a32), value(a33), value(a34)],
    [value(a41), value(a42), value(a43), value(a44)]
]

# Calculamos el determinante de la matriz 4x4
print("Determinante de la matriz 4x4:", determinante(matriz_4x4))

