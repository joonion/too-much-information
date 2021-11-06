from math import sqrt

def createGraph(N):
    squares = [i**2 for i in range(2, int(sqrt(2*N-1)) + 1)]
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i + j) in squares:
                graph[i].append(j)
                graph[j].append(i)
    return graph        

N = 32
graph = createGraph(32)
for v in graph.keys():
    print(v, ":", graph[v])
