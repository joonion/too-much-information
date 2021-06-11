from math import sqrt
from itertools import permutations
import heapq

def count_inversions(board):
    count = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                count += 1
    return count

def is_solvable(n, board):
    if n % 2 == 1:
        return count_inversions(board) % 2 == 0
    else:
        row_blank = board.index(0) // n
        if row_blank % 2 == 0:
            return count_inversions(board) % 2 == 1
        else:
            return count_inversions(board) % 2 == 0

def state_to_int(state):
    s = ""
    for i in range(len(state)):
        s += str(state[i])
    return int(s)

def int_to_state(v):
    s = str(v)
    if len(s) != N:
        s = "0" + s
    return list(map(int, s))

def get_neighbors(u):
    state = int_to_state(vtos[u])
    pos_blank = state.index(0)
    row, col = pos_blank // n, pos_blank % n
    neighbors = []
    for i in range(len(dir)):
        nextrow, nextcol = row + dir[i][0], col + dir[i][1]
        if 0 <= nextrow < n and 0 <= nextcol < n:
            pos_next = nextrow * n + nextcol
            board = state[:]
            board[pos_blank], board[pos_next] = board[pos_next], board[pos_blank]
            neighbors.append(stov[state_to_int(board)])
    return neighbors

def dijkstra(start, target, vsize):
    length = [INF for _ in range(vsize)]
    bypass = [0 for _ in range(vsize)]
    length[start] = 0
    heap = []
    heapq.heappush(heap, (length[start], start))
    while len(heap) > 0:
        u = heapq.heappop(heap)[1]
        if u == target:
            return bypass
        for v in get_neighbors(u):
            if length[v] < 0:
                continue # skip vertices already visited.
            elif length[v] > length[u] + 1:
                length[v] = length[u] + 1
                bypass[v] = u
                heapq.heappush(heap, (length[v], v))
        length[u] = -1 # mark u as visited
    return bypass

def find_path(start, target, bypass):
    if start == target:
        return [start]
    else:
        return find_path(start, bypass[target], bypass) + [target]

if __name__ == '__main__':
    N = int(input())
    n = int(sqrt(N))
    board = []
    for i in range(n):
        board += list(map(int, input().split()))
    solved = [i for i in range(1, N)] + [0]

    if not is_solvable(n, board):
        print("해결할 수 없는 퍼즐입니다.")
    else:
        INF = 0xFFFF # infinity
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        vtos, stov = {}, {} # mapping vertex to state, and vice versa.
        for perm in permutations(solved):
            if is_solvable(n, perm):
                v, s = len(vtos), state_to_int(perm)
                vtos[v], stov[s] = s, v
        start = stov[state_to_int(solved)]
        target = stov[state_to_int(board)]
        bypass = dijkstra(start, target, len(vtos))
        path = find_path(start, target, bypass)
        for v in path[::-1]:
            state = int_to_state(vtos[v])
            for i in range(len(state)):
                print(state[i], end = " ")
                if (i % n == n - 1):
                    print()
            print()
        print('the number of steps to solve it:', len(path) - 1)
