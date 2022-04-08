def swap(x, y):
    return y, x
    
x, y = 10, 20
print("Before swap():", x, y)
x, y = swap(x, y)
print("After swap():", x, y)
