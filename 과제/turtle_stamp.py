import turtle
import random

## 함수 선언 부분 ##

def screenLefrClick(x,y):
    # 거북이의 크기를 랜덤으로 지정
    tSize = random.randrange(2,10)
    turtle.shapesize(tSize)

    # 거북이의 색깔을 랜덤으로 지정
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))

    # 거북이의 시선의 방향을 랜덤으로 지정
    tAngle = random.randrange(0,360)

    # 펜을 올리고 마우스 위치로 이동한 후 스탬프(도장)를 찍는다.
    turtle.penup()
    turtle.goto(x,y)
    turtle.left(tAngle)
    turtle.stamp()



## 변수 선언 부분 ##
turtle.title("거북이 도장 찍기")

# 거북이 모양으로 설정하는 부분
turtle.shape('turtle')

turtle.onscreenclick(screenLefrClick,1)

turtle.done()