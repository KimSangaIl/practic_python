## 학번 : 2019038041  이름 : 김상일 ##
import turtle
import math
import random

## 전역 변수 선언 부분 ##
tur1, tur2, tur3 = [None] * 3
turx1, turx2, turx3, tury1, tury2, tury3 = [0] * 6
swidth, sheight = 300, 300

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이 서로 만나게 하기')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    tur1 = turtle.Turtle('turtle')
    tur1.color('red')
    tur1.penup()
    tur2 = turtle.Turtle('turtle')
    tur2.color('green')
    tur2.penup()
    tur3 = turtle.Turtle('turtle')
    tur3.color('blue')
    tur3.penup()

    tur1.goto(-100, -100)
    tur2.goto(0, 0)
    tur3.goto(100, 100)

    tur1.speed(10)
    tur2.speed(10)
    tur3.speed(10)
    
    while True :
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        tur1.left(angle)
        tur1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        tur2.left(angle)
        tur2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        tur3.left(angle)
        tur3.forward(dist)

        turx1 = tur1.xcor()
        tury1 = tur1.ycor()
        turx2 = tur2.xcor()
        tury2 = tur2.ycor()
        turx3 = tur3.xcor()
        tury3 = tur3.ycor()

        if (-swidth / 2 <= turx1 and turx1 <= swidth / 2) and (-sheight / 2 <= tury1 and tury1 <= sheight / 2) :
            pass
        else :
            tur1.goto(-100, -100)

        if (-swidth / 2 <= turx2 and turx2 <= swidth / 2) and (-sheight / 2 <= tury2 and tury2 <= sheight / 2) :
            pass
        else :
            tur2.goto(0, 0)

        if (-swidth / 2 <= turx3 and turx3 <= swidth / 2) and (-sheight / 2 <= tury3 and tury3 <= sheight / 2) :
            pass
        else :
            tur3.goto(100, -00)

        if math.sqrt(((turx1 - turx2) * (turx1 - turx2)) + ((tury1 - tury2) * (tury1 - tury2))) <= 30 or \
           math.sqrt(((turx2 - turx3) * (turx2 - turx3)) + ((tury2 - tury3) * (tury2 - tury3))) <= 30 or \
           math.sqrt(((turx3 - turx1) * (turx3 - turx1)) + ((tury3 - tury1) * (tury3 - tury1))) <= 30 :
            tur1.turtlesize(3)
            tur2.turtlesize(3)
            tur3.turtlesize(3)
            break

    turtle.done()
            
