def make_triangle(n):
    T = [[0] * (i + 1) for i in range(n + 1)]
    for i in range(len(T)):
        for j in range(len(T[i])):
            if j == 0 or j == i:
                T[i][j] = 1
            else:
                T[i][j] = T[i - 1][j - 1] + T[i - 1][j]
    return T

n = int(input("Input the number of n: "))
T = make_triangle(n)
for i in range(len(T)):
    for j in range(len(T[i])):
        print(T[i][j], end = " ")
    print()    