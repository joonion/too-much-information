from math import sqrt

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

if __name__ == "__main__":
    N = int(input())
    n = int(sqrt(N))
    board = []
    for i in range(n):
        board += list(map(int, input().split()))
    solved = [i for i in range(1, N)] + [0]

    if is_solvable(n, board):
        print("Solvable!")
    else:
        print("Not Solvable!")
