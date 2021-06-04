def nearest(s, length):
    minimum, vnear = INF, s
    for v in range(len(length)):
        if v == s: continue
        if 0 <= length[v] < minimum: 
            minimum, vnear = length[v], v
    return vnear

def dijkstra(s, n, W):
    bypass = [s for _ in range(n)]
    length = [W[s][i] for i in range(n)]
    for _ in range(n - 1):
        vnear = nearest(s, length)
        for v in range(n):
            if length[v] > length[vnear] + W[vnear][v]:
                length[v] = length[vnear] + W[vnear][v]
                bypass[v] = vnear
        length[vnear] = -1
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

s, t = 0, 9
bypass = dijkstra(s, n, W)
path = shortest(s, t, bypass)
print(bypass)
print(path)
