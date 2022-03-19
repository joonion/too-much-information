def make_triangle(n):
    T = [[0] * (i + 1) for i in range(n + 1)]
    for i in range(len(T)):
        for j in range(len(T[i])):
            if j == 0 or j == i:
                T[i][j] = 1
            else:
                T[i][j] = T[i - 1][j - 1] + T[i - 1][j]
    return T

n = 15
T = make_triangle(n)

for i in range(n + 1):
    row, col = i, 0
    S = 0
    while row >= 0 and col <= row:
        S += T[row][col]
        row, col = row - 1, col + 1
    print(S, end = " ")
print()

a, b = 1, 1
print(a, end = " ")
print(b, end = " ")
for i in range(n - 1):
    a, b = b, (a + b)
    print(b, end = " ")
print()