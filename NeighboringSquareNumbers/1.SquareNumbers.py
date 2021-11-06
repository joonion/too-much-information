from math import sqrt

N = 32
squares = [i**2 for i in range(2, int(sqrt(2*N-1)) + 1)]
print(squares)

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if (i + j) in squares:
            print(i, j)

