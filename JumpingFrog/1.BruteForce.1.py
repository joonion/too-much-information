def visitable(circle):
    pos = 0
    while circle[pos] > 0:
        next_pos = (pos + circle[pos]) % len(circle)
        circle[pos] = 0
        pos = next_pos
    return sum(circle) == 0

circle = [1, 2, 3, 4]
print(visitable(circle))

circle = [1, 2, 4, 3]
print(visitable(circle))
