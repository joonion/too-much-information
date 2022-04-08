def swap(x, y):
    x, y = y, x
    print("Inside swap():", x, y)
    
x, y = 10, 20
print("Before swap():", x, y)
swap(x, y)
print("After swap():", x, y)
