## 2019038041 김상일 ##

import turtle
import random

## 함수 선언 부분 ##
def screenRightClick(x, y) :
    global r, g, b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.color((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    tAngle = random.randrange(0,360)
    turtle.right(tAngle)
    turtle.stamp()

## 변수 선언 부분 ##
pSize = 3
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이 도장찍기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenRightClick, 3)

turtle.done()
