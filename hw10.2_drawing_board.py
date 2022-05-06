## 2019038041 김상일 ##
from tkinter import *
from tkinter.simpledialog import *
from tkinter.colorchooser import *

## Function ##
def linecolor():
    global pcolor
    color = askcolor()
    pcolor = color[1]

def linept():
    global pt
    pt = askinteger("선 두께", "선 두께(1~10)를 입력하세요.", minvalue = 1, maxvalue = 10)

def click(po):
    global x1, x2, y1, y2
    x1 = po.x
    y1 = po.y

def nclick(po):
    global x1, x2, y1, y2, pcolor, pt
    x2 = po.x
    y2 = po.y
    canvas.create_line(x1, y1, x2, y2, width = pt, fill = pcolor)

## Variable ##
window = None
canvas = None
x1, x2, y1, y2, = [None] * 4
pcolor = 'black'
pt = 5

## Main Code ##
if __name__ == "__main__":
    window = Tk()
    window.title("그림판 비슷한 프로그램")

    canvas = Canvas(window, width = 500, height = 500)
    canvas.bind("<Button-1>", click)
    canvas.bind("<ButtonRelease-1>", nclick)
    canvas.pack()

    setting = Menu(window)
    window.config(menu = setting)

    settinglist = Menu(setting)
    setting.add_cascade(label = "설정", menu = settinglist)
    settinglist.add_command(label = "선 색상 선택", command = linecolor)
    settinglist.add_separator()
    settinglist.add_command(label = "선 두께 설정", command = linept)

    window.mainloop()