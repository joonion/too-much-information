def hanoi(n, src, dst, via):
    if n == 1:
        print(f"{src} -> {dst}")
    else:
        hanoi(n - 1, src, via, dst)
        print(f"{src} -> {dst}")
        hanoi(n - 1, via, dst, src)        

n = 3
hanoi(3, 1, 3, 2)    