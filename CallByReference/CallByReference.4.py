def swap(x, y):
    t = x
    x = y
    y = t
    print("Inside swap():", x, y)
    
x, y = 10, 20
print("Before swap():", x, y)
swap(x, y)
print("After swap():", x, y)
