from itertools import permutations 
w1, w2, w3 = "SEND", "MORE", "MONEY"
letters = sorted(set(w1 + w2 + w3))
digits = list(range(10))
print(letters, digits)
perms = list(permutations(digits, len(letters)))
print(len(perms))
