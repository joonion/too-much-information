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
    print(sum(T[i]), end = " ")
print()

for i in range(n + 1):
    print(2 ** i, end = " ")
print()