## 학번: 2019038041 이름: 김상일 ##
import turtle
import random

## 전역 변수 선언 부분 ##
myturtle, tx, ty, tcolor, tsize, tangle, = [None] * 6
playerturtles = []
swidth, sheight = 500, 500

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('랜덤 크기 거북이 정렬')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    for i in range(0,5) :
        myturtle = turtle.Turtle('turtle')
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight / 2, sheight / 2)
        r = random.random()
        g = random.random()
        b = random.random()
        tangle = random.randrange(0, 360)
        tsize = random.randrange(1, 100)/10
        playerturtles.append([myturtle, tx, ty, tsize, tangle, r, g, b])

    sortedturtles = sorted(playerturtles, key = lambda turtles : turtles[3], reverse = True)

    for index, tlist in enumerate(sortedturtles[0:]) :
        myturtle = tlist[0]
        myturtle.color((tlist[5], tlist[6], tlist[7]))
        myturtle.pencolor((tlist[5], tlist[6], tlist[7]))
        myturtle.turtlesize(tlist[3])
        myturtle.left(tlist[4])
        myturtle.penup()
        if index == 0 :
            myturtle.goto(tlist[1], tlist[2])
            continue
        myturtle.goto(sortedturtles[index-1][1], sortedturtles[index-1][2])
        myturtle.pendown()
        myturtle.goto(tlist[1], tlist[2])

    turtle.done()
