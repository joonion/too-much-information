def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
if __name__=='__main__':
    n = int(input("input n: "))
    f = fibonacci(n)
    print(f"F({n}) is {f}.")    
    