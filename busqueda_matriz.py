# Programa 1: Búsqueda en Arreglo Multidimensional

# Matriz bidimensional 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna posición (fila, columna)
    return None

# Valor a buscar
valor_buscado = 50

# Búsqueda
posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"✅ El valor {valor_buscado} se encontró en la posición (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"❌ El valor {valor_buscado} no se encontró en la matriz.")

