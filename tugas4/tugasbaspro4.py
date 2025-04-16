# Matriks A dan B (5x5) dengan angka baru
A = [
    [2, 4, 1, 3, 5],
    [6, 7, 3, 8, 2],
    [9, 5, 2, 6, 4],
    [1, 3, 7, 9, 0],
    [4, 8, 6, 2, 1]
]

B = [
    [5, 2, 1, 6, 3],
    [3, 0, 4, 2, 1],
    [6, 1, 7, 0, 5],
    [1, 3, 2, 4, 8],
    [0, 9, 3, 1, 7]
]

# Inisialisasi matriks hasil 5x5 dengan nilai 0
result = [[0 for _ in range(5)] for _ in range(5)]

# Perkalian matriks
for i in range(5):
    for j in range(5):
        for k in range(5):
            result[i][j] += A[i][k] * B[k][j]

# Fungsi untuk mencetak matriks dengan rapi
def print_matrix(matrix, name):
    print(f"Matriks {name}:")
    for row in matrix:
        print(row)
    print()

# Cetak Matriks A, B, dan Hasil
print_matrix(A, "A")
print_matrix(B, "B")
print_matrix(result, "A x B")