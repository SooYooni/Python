
import turtle as t
l = int(input("Enter the height of the Rextangle:"))
w = int(input("Enter the width of the Rectangle:"))

for i in range(4):

    if i % 2 == 0:
        t.forward(l)
        t.left(90)

    else:
        t.forward(w)
        t.left(90)

t.done()