def visitable(circle):
    pos = 0
    while circle[pos] > 0:
        next_pos = (pos + circle[pos]) % len(circle)
        circle[pos] = 0
        pos = next_pos
    return sum(circle) == 0

from itertools import permutations

for n in range(1, 13):
    nums = [i for i in range(2, n + 1)]
    perms = list(permutations(nums))
    count = 0
    for i in range(len(perms)):
        circle = [1] + list(perms[i])
        if visitable(circle[:]):
            count += 1
    print(n, ":", count) 
               