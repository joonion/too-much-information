count = 0

def createGraph(N):
    squares = [i**2 for i in range(2, int((2*N-1)**(1/2)) + 1)]
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i + j) in squares:
                graph[i].append(j)
                graph[j].append(i)
    return graph        

def hamiltonPath(graph, vertex, path):
    global count
    if len(path) == len(graph):
        # print("solution", path)
        count += 1
    else:
        for neighbor in graph[vertex]:
            if neighbor not in path:
                path.append(neighbor)
                hamiltonPath(graph, neighbor, path)
                path.pop()

def solve(N):
    global count
    count = 0
    graph = createGraph(N)
    path = [1]
    hamiltonPath(graph, path[0], path)
    print("The number of solutions for", N, "is", count)

def main():
    for N in range(1, 33):
        solve(N)

main()
