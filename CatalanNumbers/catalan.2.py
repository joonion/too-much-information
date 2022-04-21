# Catalan Numbers using Memoization (+ Recursion)

def catalan(n, C):
    if n == 0:
        C[n] = 1
    else:
        if C[n] == 0:
            for i in range(n):
                C[n] += catalan(i, C) * catalan(n - i - 1, C)
    return C[n]

n = 20
C = [0] * (n + 1)
for i in range(n + 1):
    print(i, catalan(i, C))