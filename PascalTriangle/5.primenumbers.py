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


for i in range(2, n + 1):
    print(i, end = ": ")
    for j in range(i + 1):
        print(T[i][j] % i, end = " ")
    print()

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
    return True

for i in range(2, n + 1):
    if is_prime(i):
        print(i, end = ": ")
        for j in range(1, i):
            print(T[i][j] % i, end = " ")
        print()
