dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()

def move(dir, cx, cy, maze, mark):
    nx, ny = cx + dx[dir], cy + dy[dir]
    n, m = len(maze), len(maze[0])
    if not (0 <= nx < n and 0 <= ny < m):
        return False, nx, ny
    if maze[nx][ny] == 0 or mark[nx][ny] == 1:
        return False, nx, ny
    return True, nx, ny
    
def solve(sx, sy, ex, ey, maze, mark):
    if (sx, sy) == (ex, ey):
        print(path)
        return
    else:
        for i in range(4):
            canMove, nx, ny = move(i, sx, sy, maze, mark)
            if canMove:
                mark[sx][sy] = 1
                solve(nx, ny, ex, ey, maze, mark)

n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
maze = [[0] * m for _ in range(n)]
mark = [[0] * m for _ in range(n)]
for i in range(n):
    maze[i] = list(map(int, input().split()))

path = []
solve(sx, sy, ex, ey, maze, mark, path)
