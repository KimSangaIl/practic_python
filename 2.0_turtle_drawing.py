import turtle
import random

## declare function ##
def screenleftclick(x, y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenrightclick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

def screenmidclick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## declare global variable ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## main code ##
turtle.title('drawing turtle')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenleftclick, 1)
turtle.onscreenclick(screenmidclick, 2)
turtle.onscreenclick(screenrightclick, 3)

turtle.done()
