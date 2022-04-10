def perm(n, S):
    if n <= 1:
        return 1
    else:
        C = 0
        for i in range(n):
            P, Q = S[:i], S[(i+1):]
            C += perm(i, P) * perm(n - i - 1, Q)
        return C
    
S = list("A")
C = perm(len(S), S)
print(C)