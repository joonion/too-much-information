import turtle as t

t.right(30)
def triangle(size):
    for i in range(3):
        t.forward(size)
        t.right(120)

if __name__=='__main__':
    t.right(30)
    triangle(200)
    input("Press any key...")

