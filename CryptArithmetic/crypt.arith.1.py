w1, w2, w3 = "SEND", "MORE", "MONEY"

letters = sorted(set(w1 + w2 + w3))
digits = list(range(10))
print(letters, digits)

from itertools import permutations

perms = list(permutations(digits, len(letters)))
print(len(perms))

for perm in perms:
    map = {k:v for k, v in zip(letters, perm)}
    print(map)
    