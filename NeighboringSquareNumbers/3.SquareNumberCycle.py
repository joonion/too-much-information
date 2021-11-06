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

def hamiltonCycle(graph, vertex, path):
    if len(path) == len(graph) and vertex in graph[path[0]]:
        print(path)
    else:
        for neighbor in graph[vertex]:
            if neighbor not in path:
                path.append(neighbor)
                hamiltonCycle(graph, neighbor, path)
                path.pop()

N = 32
graph = createGraph(N)
path = [1]
hamiltonCycle(graph, path[0], path)

