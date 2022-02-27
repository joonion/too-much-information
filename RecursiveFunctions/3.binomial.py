def binomial(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomial(n - 1, k) + binomial(n - 1, k - 1)
    
if __name__=='__main__':
    n, k = map(int, input("input n and k: ").split())
    b = binomial(n, k)
    print(f"B({n}, {k}) is {b}")