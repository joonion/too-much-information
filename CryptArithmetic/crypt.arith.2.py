from itertools import permutations 
w1, w2, w3 = "SEND", "MORE", "MONEY"
letters = sorted(set(w1 + w2 + w3))
digits = list(range(10))
print(letters, digits)
perms = list(permutations(digits, len(letters)))

def to_int(revstr, map):
    value = 0
    for i in range(len(revstr)):
        value += map[revstr[i]] * (10 ** i)
    return value

def is_valid(w1, w2, w3, map):
    leadings = [map[w1[0]], map[w2[0]], map[w3[0]]]
    if 0 in leadings:
        return False
    a = to_int(w1[::-1], map)
    b = to_int(w2[::-1], map)
    c = to_int(w3[::-1], map)
    return a + b == c

for perm in perms:
    map = {k:v for k, v in zip(letters, perm)}
    if is_valid(w1, w2, w3, map):
        print(map)
