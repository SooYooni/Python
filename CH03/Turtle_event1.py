import turtle
import random

## 함수 선언 부분 ##
def screenLeftClick(x,y):
    global r, g, b
    global pSize

    r = random.random()
    g = random.random()
    b = random.random()
    print('r = ', r, 'g = ', g, 'b = ', b)

    pSize = random.randrange(1,10)

    turtle.pencolor((r, g, b))
    turtle.pencolor()
    turtle.goto(x, y)

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

##  메인 코드 부분 ##
turtle.title('거북이로 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.done()