def nearest(s, length):
    minimum, vnear = INF, s
    for v in range(len(length)):
        if v == s: continue
        if 0 <= length[v] < minimum: 
            minimum, vnear = length[v], v
    return vnear

def a_star(s, t, n, W, H):
    bypass = [s for _ in range(n)]
    g = [0 if i == s else INF for i in range(n)]
    h = [H[i][t] for i in range(n)]
    f = [h[s] if i == s else INF for i in range(n)]
    for _ in range(n - 1):
        vnear = nearest(s, f)
        if vnear == t: 
            return bypass
        for v in range(n):
            if g[v] > g[vnear] + W[vnear][v]:
                g[v] = g[vnear] + W[vnear][v]
                f[v] = g[v] + h[v]
                bypass[v] = vnear
        f[vnear] = -1
    return bypass

def shortest(s, t, bypass):
    if bypass[t] == s:
        return [s, t]
    else:
        return shortest(s, bypass[t], bypass) + [t]

INF = 0xFFFF
n, m = map(int, input().split())
W = [[0 if i == j else INF for i in range(n)] for j in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
H = [[0 if i == j else INF for i in range(n)] for j in range(n)]
k = int(input())
for _ in range(k):
    u, v, h = map(int, input().split())
    H[u][v] = h

s, t = 0, 9
bypass = a_star(s, t, n, W, H)
path = shortest(s, t, bypass)
print(bypass)
print(path)
