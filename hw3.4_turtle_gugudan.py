## 학번 : 2019038041  이름 : 김상일 ##
import turtle

## 전역 변수 선언 부분 ##
i, k, turx, tury = [0] * 4
swidth, sheight = 700, 400

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이 구구단')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turx, tury = -500, 200
    turtle.goto(turx, tury)

    for i in range(1, 10) :
        for k in range(2, 10) :
            turtle.goto(turx +80 * k, tury - 40 * i)
            gugu = str(k) + ' x ' + str(i) + ' = ' + str(k * i)
            turtle.write(gugu, font = ('Arial', 12, 'bold'))

    turtle.done()
