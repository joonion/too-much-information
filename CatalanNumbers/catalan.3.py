# Catalan Numbers using Dynamic Programming(Memoization + Bottom-Up)

def catalan(n):
    C = [0] * (n + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - j - 1]
    return C[n]

n = 100
for i in range(n + 1):
    print(i, catalan(i))