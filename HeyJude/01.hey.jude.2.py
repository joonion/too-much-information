lyrics = [
    "hey Jude",
    "don't",
    "make it bad",
    "be afraid",
    "let me down",
    "take a sad song and make it better",
    "you were made to go out and get her",
    "you have found her now go and get her",
    "remember to",
    "the minute you",
    "let her into your heart",
    "let her under your skin",
    "then you",
    "can start",
    "begin",
    "to make it better",
    "and anytime you feel the pain hey Jude refrain don't carry the world upon your shoulder for well you know that it's a fool who plays it cool by making his world a little colder",
    "so let it out and let it in hey Jude begin you're waiting for someone to perform with and don't you know that it's just you hey Jude you'll do the movement you need is on your shoulder",
    "better better better better better waaaaa"
]

stepStarts = [0, 1, 2, 5, 8, 10, 12, 13, 15, 16]

def pick(verse, step):
    index = stepStarts[step]
    if step in [2, 3]:
        index += verse % 3
    elif step in [4]:
        index += 1 if (verse == 1) else 0
    elif step in [5, 7]:
        index += 1 if (verse % 2 != 0) else 0
    elif step in [9]:
        index += verse - 1
    return index

for verse in range(4):
    print(verse + 1)
    for step in range(10):
        print(lyrics[pick(verse, step)], end=" ")
        if verse == 0 and step == 8:
            break
    if verse in [1, 2]:
        print("na " * 9, end=" ")
    print()
fadeout = 17
while fadeout != 0:
    print("na " * 11, end=" ")
    print(lyrics[0])
    fadeout -= 1
        