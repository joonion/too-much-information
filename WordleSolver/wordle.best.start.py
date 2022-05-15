words = []
with open('words_with_five_chars.txt', 'r') as f:
    reads = f.readlines()
    for word in reads:
        words.append(word.strip())
        
freq = [0] * 26
for word in words:
    for i in range(len(word)):
        alpha = ord(word[i]) - ord('A')
        freq[alpha] += 1
# print(freq)

prob = {}
for word in words:
    chars = list(set(list(word)))
    prod = 1
    for i in range(len(chars)):
        alpha = ord(word[i]) - ord('A')
        prod *= freq[alpha]
    prob[word] = prod
# print(prob)

largest = max(prob, key = prob.get)
print(largest, prob[largest])

test = "CRANE"
print(test, prob[test])

test = "DEALT"
print(test, prob[test])

test = "ALIEN"
print(test, prob[test])

test = "TESLA"
print(test, prob[test])

test = "TEARS"
print(test, prob[test])

test = "RAISE"
print(test, prob[test])

test = "ARISE"
print(test, prob[test])

test = "AROSE"
print(test, prob[test])

best = "RAISE"
print("==> Better than", best)
for k, v in prob.items():
    if v > prob[best]:
        print(k, v)
            