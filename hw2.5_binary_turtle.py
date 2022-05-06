## 2019038041 김상일 ##

import turtle

## 변수 선언 부분 ##
dnum, bnum = 0, 0
swidth, sheight = 700, 200
curX, curY = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 숫자 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight / 2)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    dnum = int(input('변환할 숫자 입력 : '))
    bnum = bin(dnum)
    curX = swidth / 2
    curY = 0
    for i in range(len(bnum) - 2) :
        turtle.goto(curX, curY)
        if dnum & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        dnum >>=1

turtle.done()
