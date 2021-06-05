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

verses = [
    [0, 1, 2, 5, 8, 10, 12, 13, 15],
    [0, 1, 3, 6, 9, 11, 12, 14, 15, 16],
    [0, 1, 4, 7, 8, 10, 12, 13, 15, 17],
    [0, 1, 2, 5, 8, 11, 12, 14, 15, 18]
]

for i in range(len(verses)):
    print(i + 1)
    for j in range(len(verses[i])):
        print(lyrics[verses[i][j]], end=" ")    
    if i in [1, 2]:
        print("na " * 9, end=" ")
    print()
fadeout = 17
while fadeout != 0:
    print("na " * 11, end=" ")
    print(lyrics[0])
    fadeout -= 1
