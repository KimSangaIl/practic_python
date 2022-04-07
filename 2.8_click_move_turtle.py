import turtle
import random

## declare function ##
def screenrightclick(x, y) :
    global r, g, b, tSize, tAngle
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 10)
    tAngle = random.randrange(0, 360)
    
    turtle.color((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    turtle.shapesize(tSize)
    turtle.left(tAngle)
    turtle.stamp()

## declare global variable ##
r, g, b = 0.0, 0.0, 0.0
pSize = 1

## main code ##
turtle.title('click move turtle')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenrightclick, 3)

turtle.done()
