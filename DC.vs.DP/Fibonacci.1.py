def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)
    
print(fib1(5))