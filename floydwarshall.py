import numpy as np
INF = 99999

def algoWarshall(graf):  # untuk mencari jalur terpendek (transitive closure)
    jmlhSimpul = len(graf)
    jarak = np.array(graf, dtype=int)

    for perantara_k in range(jmlhSimpul):
        for asal_i in range(jmlhSimpul):
            for tujuan_j in range(jmlhSimpul):
                jarak[asal_i][tujuan_j] = int(jarak[asal_i][tujuan_j] > 0 or (jarak[asal_i][perantara_k] > 0 and jarak[perantara_k][tujuan_j] > 0))
    return jarak

def algoFloydWarshall(graf):  # untuk mencari jarak terpendek (shortest path)
    jmlhSimpul = len(graf)
    jarak = np.array(graf, dtype=int)

    for i in range(jmlhSimpul):
        for j in range(jmlhSimpul):
            if i != j and jarak[i][j] == 0:
                jarak[i][j] = INF

    for perantara_k in range(jmlhSimpul):
        for asal_i in range(jmlhSimpul):
            for tujuan_j in range(jmlhSimpul):
                if jarak[asal_i][perantara_k] != INF and jarak[perantara_k][tujuan_j] != INF:
                    jarak[asal_i][tujuan_j] = min(
                        jarak[asal_i][tujuan_j], jarak[asal_i][perantara_k] + jarak[perantara_k][tujuan_j]
                    )
    return jarak

def printMatrix(matrix):
    for row in matrix:
        print(*(num if num != INF else "∞" for num in row))

graf0 = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]
graf1 = [
    [0, 3, 0, 0, 5],
    [0, 0, 2, 4, 0],
    [0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
graf2 = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
graf3 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
graf4 = [
    [0, 1, 0, 0, 2, 0],
    [0, 0, 3, 4, 0, 0],
    [0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print("Penutupan Transitif (Algoritma Warshall):")
printMatrix(algoWarshall(graf4))

print("Jarak Terpendek (Algoritma Floyd-Warshall):")
printMatrix(algoFloydWarshall(graf4))