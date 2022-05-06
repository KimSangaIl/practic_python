## 2019038041 김상일 ##
from tkinter import *
from tkinter.filedialog import *

## Function ##
def openfile():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*. *")))
    photo = PhotoImage(file = filename)
    label1.configure(image = photo)
    label1.image = photo

def updown(event):
    global updown
    updown = event.keysym
    mul = 2
    photo = PhotoImage(file = filename)

    if (updown == "Up"): photo = photo.zoom(mul, mul)
    elif (updown == "Down"): photo = photo.subsample(mul, mul)
    
    label1.configure(image = photo)
    label1.image = photo

## Main Code ##
if __name__ == "__main__":
    window = Tk()
    window.title("사진 감상하기")
    window.geometry("500x500")

    mainmenu = Menu(window)
    window.config(menu = mainmenu)

    filemenu = Menu(mainmenu)
    mainmenu.add_cascade(label = "파일", menu = filemenu)
    filemenu.add_command(label = "파일 열기", command = openfile)
    filemenu.add_separator()
    filemenu.add_command(label = "프로그램 종료", command = quit)

    photo = PhotoImage()
    label1 = Label(window, image = photo)
    label1.pack(expand = 1, anchor = CENTER)

    window.bind("<Key>", updown)

    window.mainloop()