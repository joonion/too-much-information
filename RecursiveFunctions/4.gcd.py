def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
if __name__=='__main__':
    n, m = map(int, input("input n and m: ").split())
    cd = gcd(n, m)
    print(f"gcd({n}, {m}) is {cd}")