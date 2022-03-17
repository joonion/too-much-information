# Solve Tromino Puzzle with the Divide-and-Conquer Strategy
# [input] n row col
# n is the size of board and (row, col) is a given hole.
# [output] n * n board placed with trominoes
# a tromino is shown with L-shaped n which is the size of board 
# when a recursive function is called.

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()

def whereis(n, srow, scol, row, col):
    m = n // 2
    if row - srow < m:
        return 1 if col - scol < m else 2
    else:
        return 3 if col - scol < m else 4

def fill(n, board, srow, scol, where):
    if where != 1: board[srow][scol]     = n
    if where != 2: board[srow][scol+1]   = n
    if where != 3: board[srow+1][scol]   = n
    if where != 4: board[srow+1][scol+1] = n

def hole(part, where, n, srow, scol, row, col):
    m = n // 2
    if part != where:
        row, col = srow + m - 1, scol + m - 1
        if part == 2 or part == 4: col += 1
        if part == 3 or part == 4: row += 1
    return row, col

def tromino(n, board, srow, scol, row, col):
    where = whereis(n, srow, scol, row, col)
    if n == 2:
        fill(n, board, srow, scol, where)
    else:
        m = n // 2
        fill(n, board, srow + m - 1, scol + m - 1, where)
        hrow, hcol = hole(1, where, n, srow, scol, row, col)
        tromino(m, board, srow, scol, hrow, hcol)
        hrow, hcol = hole(2, where, n, srow, scol, row, col)
        tromino(m, board, srow, scol+m, hrow, hcol)
        hrow, hcol = hole(3, where, n, srow, scol, row, col)
        tromino(m, board, srow+m, scol, hrow, hcol)
        hrow, hcol = hole(4, where, n, srow, scol, row, col)
        tromino(m, board, srow+m, scol+m, hrow, hcol)

n, row, col = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
srow, scol = 0, 0
tromino(n, board, srow, scol, row, col)
print_board(board);
