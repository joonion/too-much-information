# Does word exclude every characters in s?
def check_excludes(word, s):
    for c in s:
        if c in word:
            return False
    return True

# Does word include every characters in s?
def check_includes(word, s):
    for c in s:
        if c not in word:
            return False
    return True

# Does given characters are well positioned?
def check_position(word, pmap):
    for key in pmap:
        if word[key] != pmap[key]:
            return False
    return True

# Read words from the dictionary
words = []
with open('words_with_five_chars.txt', 'r') as f:
    reads = f.readlines()
    for word in reads:
        words.append(word.strip())

# Prepare the constraints you have found
includes = 'ALT'    # characters that should be included
excludes = 'DSP'    # characters that should be excluded
positions = {1:'E'} # characters of which the position has been found

# Check the constraints you have been found
recommend = []
for word in words:
    if not check_position(word, positions):
        continue
    if not check_includes(word, includes):
        continue
    if not check_excludes(word, excludes):
        continue
    recommend.append(word)

# List the words that is recommended to try.
for word in recommend:
    print(word)
  
'''  
More Hint: Start it with 'CRANE' or 'DEALT'.
Mathematicians have found that staring with these words makes it possible 
to find the solution more efficiently with higer probability
'''
