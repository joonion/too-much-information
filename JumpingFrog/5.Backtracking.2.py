def jump(n, circle, pos):
    if len(circle) == n:
        print("solution:", end=" ")
        for i in range(n):
            print(circle[i], end=" ")
        print()
    else:
        next_pos = (pos + circle[pos]) % n
        if next_pos not in circle:
            for k in range(1, n + 1):
                if k not in circle.values():
                    circle[next_pos] = k
                    jump(n, circle, next_pos)
                    circle.pop(next_pos)

n = 12
circle = {0:1}
jump(n, circle, 0)
