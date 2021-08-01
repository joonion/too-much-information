F = {}

def fib3(n):
    F[1] = F[2] = 1
    for i in range(3, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

print(fib3(5))
print(F)
