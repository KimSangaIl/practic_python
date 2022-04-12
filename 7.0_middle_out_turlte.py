import turtle
import random

swidth, sheight = 500, 500
mytu, tx, ty, tc, ts, tsh = [None] * 6
shlist = []
tulist = []

if __name__ == "__main__":
    turtle.title('밖으로 나가는 거북이')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    shlist = turtle.getshapes()
    for i in range(0, 100):
        random.shuffle(shlist)
        mytu = turtle.Turtle(shlist[0])
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight / 2, sheight / 2)
        r = random.random()
        g = random.random()
        b = random.random()
        ts = random.randrange(1, 3)
        tulist.append([mytu, tx, ty, r, g, b, ts])
    
    for tlist in tulist:
        mytu = tlist[0]
        mytu.color((tlist[3], tlist[4], tlist[5]))
        mytu.pencolor((tlist[3], tlist[4], tlist[5]))
        mytu.turtlesize(tlist[6])
        mytu.goto(tlist[1], tlist[2])
    turtle.done()