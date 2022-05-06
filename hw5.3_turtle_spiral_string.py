## 학번: 2019038041 이름: 김상일 ##
import turtle
import math
import random
from tkinter.simpledialog import *

## 전역 변수 선언 ##
inss = ""
swidth, sheight = 500, 500
txtsize = 20
radius = 200
tx, ty, angle, radian, count = 0, 0, 0, 0, 0

## 메인 코드 ##
turtle.title('거북이 나선형 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inss = askstring('문자열 입력', '거북이가 쓸 문자열을 입력')
angle = 360 * 2 / len(inss)

for ch in inss :
    tx = radius * math.cos(-radian)
    ty = radius * math.sin(-radian)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.goto(tx, ty)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtsize, 'bold'))
    radius = radius - (200 / len(inss))
    count += 1
    radian = 3.14 * (720 - (angle * count)) / 180

turtle.done()
