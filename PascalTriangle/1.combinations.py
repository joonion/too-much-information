from math import factorial

n = 15

for i in range(n + 1):
    for j in range(i + 1):
        iCj = factorial(i) // factorial(j) // factorial(i - j)
        print(iCj, end = " ")
    print()        