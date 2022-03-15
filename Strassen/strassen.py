# Matrix Multiplication by the Strassen's Method
# Time Complexity = O(n^log2(7)) ~ O(n^2.81)

threshold = 1

def print_matrix(M):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")
        print()

def madd(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def msub(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mmult(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def partition(M):
    n, m = len(M), len(M) // 2
    M11 = [[M[i][j] for j in range(m)] for i in range(m)]
    M12 = [[M[i][j] for j in range(m, n)] for i in range(m)]
    M21 = [[M[i][j] for j in range(m)] for i in range(m, n)]
    M22 = [[M[i][j] for j in range(m, n)] for i in range(m, n)]
    return M11, M12, M21, M22

def combine(M11, M12, M21, M22):
    n, m = 2 * len(M11), len(M11)
    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for j in range(m):
            M[i][j]         = M11[i][j]
            M[i][m + j]     = M12[i][j]
            M[m + i][j]     = M21[i][j]
            M[m + i][m + j] = M22[i][j]
    return M

def strassen(A, B):
    n = len(A)
    if n <= threshold:
        return mmult(A, B)
    else:
        # Divide A and B into 4 submatrices
        A11, A12, A21, A22 = partition(A)
        B11, B12, B21, B22 = partition(B)
        # Conquer by applying the Strassen's Method
        M1 = strassen(madd(A11, A22), madd(B11, B22))
        M2 = strassen(madd(A21, A22), B11)
        M3 = strassen(A11, msub(B12, B22))
        M4 = strassen(A22, msub(B21, B11))
        M5 = strassen(madd(A11, A12), B22)
        M6 = strassen(msub(A21, A11), madd(B11, B12))
        M7 = strassen(msub(A12, A22), madd(B21, B22))
        C11 = madd(msub(madd(M1, M4), M5), M7)
        C12 = madd(M3, M5)
        C21 = madd(M2, M4)
        C22 = madd(msub(madd(M1, M3), M2), M6)
        return combine(C11, C12, C21, C22)

n = int(input())
A = [[] for _ in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
B = [[] for _ in range(n)]
for i in range(n):
    B[i] = list(map(int, input().split()))

C = mmult(A, B)
print("Multiplied by the naive method:")
print_matrix(C)

D = strassen(A, B)
print("Multiplied by the Strassen's method:")
print_matrix(D)
