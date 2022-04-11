import turtle
import random

swidth, sheight = 500, 500
tx, ty, r, g, b = 0, 0, 0, 0, 0
dis = 0

if __name__ == "__main__":
    turtle.title('drawing star turtle')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.pensize(3)
    turtle.speed(5)

    while True:
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight / 2, sheight / 2)
        dis = random.randrange(10, 200)
        r = random.random()
        g = random.random()
        b = random.random()

        turtle.goto(tx, ty)
        turtle.pencolor((r, g, b))
        turtle.pendown()
        for i in range(0, 5):
            turtle.forward(dis)
            turtle.left(144)
        turtle.penup()
