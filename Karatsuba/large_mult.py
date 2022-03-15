# Divide-and-Conquer for Large Integer Multiplication
# Time Complexity = O(n^2)

threshold = 1

def large_mult(u, v):
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
        p1, p2 = large_mult(x, w), large_mult(x, z)
        p3, p4 = large_mult(w, y), large_mult(y, z)
        return p1*(10**(2*m)) + (p2 + p3)*(10**m) + p4

u, v = map(int, input().split())
print(u*v)
uv = large_mult(u, v)
print(uv)
