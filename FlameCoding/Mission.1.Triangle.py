import turtle as t
<<<<<<< HEAD
import time 

t.forward(100)
t.right(90)
time.sleep(0.5)
t.forward(100)
t.right(90)
time.sleep(0.5)
t.forward(100)
t.right(90)
time.sleep(0.5)
t.forward(100)

input("Press any key to exit ...")
=======
import time

t.title("Rectangle")
t.setup(540, 960)
t.shape("turtle")
t.bgcolor("white")
t.pencolor("red")
t.fillcolor("red")
t.pensize(2)
t.speed(1)
t.showturtle()
input("Press any key to continue...")

for i in range(4):
    t.forward(200)
    t.right(90)

input("Press any key to exit...")
>>>>>>> b918701ca20014918dc09a30e25579ed90167d72
