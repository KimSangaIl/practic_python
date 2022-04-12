import turtle
import random

swidth, sheight = 500, 500
mt, ta, ts, tx, ty, r, g, b = [None] * 8
pt = []

if __name__ == "__main__":
    turtle.title('거북이 크기순 정렬')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    for i in range(0, 5):
        mt = turtle.Turtle('turtle')
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight /2 , sheight / 2)
        r = random.random()
        g = random.random()
        b = random.random()
        ta = random.randrange(0, 360)
        ts = random.randrange(1, 100)/10
        pt.append([mt, tx, ty, r, g, b, ta, ts])
    
    sortedturtles = sorted(pt, key = lambda turtles : turtles[7], reverse = True)

    for index, tlist in enumerate(sortedturtles[0:]):
        mt = tlist[0]
        mt.color((tlist[3], tlist[4], tlist[5]))
        mt.pencolor((tlist[3], tlist[4], tlist[5]))
        mt.left(tlist[6])
        mt.shapesize(tlist[7])
        mt.penup()
        if index == 0:
            mt.goto(tlist[1], tlist[2])
            continue
        mt.goto(sortedturtles[index -1][1], sortedturtles[index -1][2])
        mt.pendown()
        mt.goto(tlist[1], tlist[2])
    turtle.done()