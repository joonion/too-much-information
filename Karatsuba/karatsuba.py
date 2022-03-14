# Karatsuba Algorithm for Large Integer Multiplication
# Time Complexity = O(n^lg3) ~ O(n^1.58)

threshold = 1

def karatsuba(u, v):
    global threshold
    n = max(len(str(u)), len(str(v)))
    if u == 0 or v == 0:
        return 0
    elif n <= threshold:
        return u * v
    else:
        m = n // 2
        x, y = u // (10**m), u % (10**m)
        w, z = v // (10**m), v % (10**m)
        r = karatsuba(x + y, w + z)
        p = karatsuba(x, w)
        q = karatsuba(y, z)
        return p*(10**(2*m)) + (r - p - q)*(10**m) + q
        
u, v = map(int, input().split())
print(u*v)
uv = karatsuba(u, v)
print(uv)
