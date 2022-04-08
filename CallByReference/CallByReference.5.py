def swap(x, y):
    return y, x
    
x, y = 10, 20
print("Before swap():", x, y)
x, y = y, x
print("After swap():", x, y)
