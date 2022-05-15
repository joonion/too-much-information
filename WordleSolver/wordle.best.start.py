words = []
with open('words_with_five_chars.txt', 'r') as f:
    reads = f.readlines()
    for word in reads:
        words.append(word.strip())
        
freq = [[0] * 26 for _ in range(5)]
for word in words:
    for i in range(len(word)):
        alpha = ord(word[i]) - ord('A')
        freq[i][alpha] += 1
        
# for f in freq:
#     print(f)

prob = {}
for word in words:
    psum = 1
    for i in range(len(word)):
        alpha = ord(word[i]) - ord('A')
        psum *= freq[i][alpha]
    prob[word] = psum
    
largest = max(prob, key = prob.get)
print(largest, prob[largest])

test = "CRANE"
print(test, prob[test])

test = "DEALT"
print(test, prob[test])

# for k, v in prob.items():
#     if v > 3566532742498232:
#         print(k, v)
            