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

import networkx as nx

N = 32
graph = createGraph(N)
nxgraph = nx.Graph()
nxgraph.add_nodes_from([i for i in range(1, N + 1)])
for u in graph.keys():
    for v in graph[u]:
        nxgraph.add_edge(u, v)
pos = nx.spectral_layout(nxgraph)
nx.draw_networkx(nxgraph, pos=pos, with_labels=True)

import networkx as nx
solution = [1, 8, 28, 21, 4, 32, 17, 19, 30, 6, 3, 13, 12, 24, 25, 11, 5, 31, 18, 7, 29, 20, 16, 9, 27, 22, 14, 2, 23, 26, 10, 15]
nxg = nx.Graph()
nxg.add_nodes_from([i for i in range(1, N + 1)])
for i in range(len(solution)):
    nxg.add_edge(solution[i - 1], solution[i])
pos = nx.spectral_layout(nxg)
nx.draw_networkx(nxg, pos=pos, with_labels=True)
