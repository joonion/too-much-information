from itertools import permutations 
from time import time

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

def solve(w1, w2, w3):
    solutions = []
    letters = sorted(set(w1 + w2 + w3))
    digits = list(range(10))
    perms = list(permutations(digits, len(letters)))
    for perm in perms:
        map = {k:v for k, v in zip(letters, perm)}
        if is_valid(w1, w2, w3, map):
            solutions.append(map.copy())
    return solutions

w1, w2, w3 = input("단어 입력:").split()
start = time()
solutions = solve(w1, w2, w3)
print("찾은 해답의 개수:", len(solutions))
for map in solutions:
    print(w1, to_int(w1[::-1], map))
    print(w2, to_int(w2[::-1], map))
    print(w3, to_int(w3[::-1], map))
print("걸린 시간:", time() - start)    
