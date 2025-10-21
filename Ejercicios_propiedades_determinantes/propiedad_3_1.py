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

def multiplicar_fila(matriz, fila_index, escalar):
    nueva_matriz = []
    for i, fila in enumerate(matriz):
        if i == fila_index:
            nueva_fila = [escalar * elemento for elemento in fila]
        else:
            nueva_fila = fila[:]
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

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

a11.setInitialValue(3)
a12.setInitialValue(7)
a13.setInitialValue(1)
a21.setInitialValue(6)
a22.setInitialValue(2)
a23.setInitialValue(8)
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

# Multiplicamos la fila 1 (segunda fila) por un escalar
escalar = 5
matriz_modificada = multiplicar_fila(matriz_original, fila_index=1, escalar=escalar)

# Calculamos determinante modificado
det_modificado = determinante(matriz_modificada)

# Mostramos resultados
print("Determinante original:", det_original)
print(f"Determinante tras multiplicar fila 1 por {escalar}:", det_modificado)
print("Relación esperada:", escalar, "×", det_original)
