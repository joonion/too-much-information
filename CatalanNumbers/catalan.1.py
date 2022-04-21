# Catalan Numbers using Recursion

def catalan(n):
    if n == 0:
        return 1
    else:
        C = 0
        for i in range(n):
            C += catalan(i) * catalan(n - i - 1)
        return C

n = 20
for i in range(n + 1):
    print(i, catalan(i))