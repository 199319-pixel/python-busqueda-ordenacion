# Programa 2: Ordenación de una fila específica de la matriz

# Matriz bidimensional 3x3
matriz = [
    [9, 3, 7],
    [4, 8, 1],
    [6, 2, 5]
]

# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar matriz original
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar matriz después de ordenar la fila
print("\n✅ Matriz después de ordenar la fila 1:")
for fila in matriz:
    print(fila)
