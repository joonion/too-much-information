def jump(n, circle, pos):
    global count
    if len(circle) == n:
        count += 1
    else:
        next_pos = ((pos + circle[pos]) % n)
        if next_pos not in circle:
            for k in range(1, n + 1):
                if k not in circle.values():
                    circle[next_pos] = k
                    jump(n, circle, next_pos)
                    circle.pop(next_pos)

for n in range(1, 15):
    circle = {0:1}
    count = 0
    jump(n, circle, 0)
    print(n, ":", count)
