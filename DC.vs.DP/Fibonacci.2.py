F = {1:1, 2:1}

def fib2(n):
    if n in F:
        return F[n]
    else:
        F[n] = fib2(n - 1) + fib2(n - 2)
        return F[n]

print(fib2(5))
print(F)