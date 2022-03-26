import turtle as t
import random

t.shape('turtle')
t.pensize(5)


def drawCircle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)

def randomDrawCircle(x, y):
    '''rX = random.randrange(1, 150)
    rY = random.randrange(1, 200)
    print('rX = ', rX, 'rY = ', rY)'''

    for _ in range(0, 50):
        rX = random.randrange(-600, 600)
        rY = random.randrange(-600, 600)
        t.penup()
        t.goto(rX, rY)
        t.pendown()
        t.circle(50)


t.onscreenclick(drawCircle, 1)
t.onscreenclick(randomDrawCircle, 2)

rX, rY = 0, 0

t.done()