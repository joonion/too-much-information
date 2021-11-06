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

def cycleCount(graph, vertex, path):
    global count
    if len(path) == len(graph) and vertex in graph[path[0]]:
        count += 1
    else:
        for neighbor in graph[vertex]:
            if neighbor not in path:
                path.append(neighbor)
                cycleCount(graph, neighbor, path)
                path.pop()

count = 0
for N in range(2, 36):
    graph = createGraph(N)
    path = [1]
    count = 0
    cycleCount(graph, path[0], path)
    print(f"The number of solutions for {N} is {count//2}.")

