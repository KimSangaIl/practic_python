import turtle

swidth, sheight = 700, 300
n1, n2, res = 0, 0, 0

if __name__ == "__main__":
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    n1 = int(input('2진수를 입력하세요: '), 2)
    n2 = int(input('2진수를 입력하세요: '), 2)
    bn1 = bin(n1)
    bn2 = bin(n2)
    res = n1 | n2
    bres = bin(res)
    curX = swidth / 2
    curY = sheight / 2 - 50

    for i in range(len(bn1) - 2):
        turtle.goto(curX, curY)
        if n1 & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        n1 >>= 1

    curX = swidth / 2
    curY -= 100
    for i in range(len(bn2) - 2):
        turtle.goto(curX, curY)
        if n2 & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        n2 >>= 1

    curX = swidth / 2
    curY -= 100
    for i in range(len(bres) - 2):
        turtle.goto(curX, curY)
        if res & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        res >>= 1
    
    turtle.done()