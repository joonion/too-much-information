def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__=='__main__':
    n = int(input("input n: "))
    f = factorial(n)
    print(f"{n}! is {f}")