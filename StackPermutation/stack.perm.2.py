def perm(n, S):
    if n <= 1:
        return S
    else:
        R = []
        for i in range(n):
            P = perm(i, S[:i])
            Q = perm(n - i - 1, S[(i+1):])
            if len(P) == 0:
                for q in Q:
                    R.append(S[i] + q)
            elif len(Q) == 0:
                for p in P:
                    R.append(S[i] + p)
            else:
                for p in P:
                    for q in Q:
                        R.append(S[i] + p + q)
        return R
    
S = list("ABCDEFG")
R = perm(len(S), S)
for r in R:
    print(r)
print(len(R))