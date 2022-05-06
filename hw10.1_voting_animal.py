## 2019038041 김상일 ##
from tkinter import *

## Function ##
def getphoto():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    else:
        labelImage.configure(image = photo3)

## Main Code ##
if __name__ == "__main__":
    window = Tk()
    window.geometry("500x500")
    window.title("애완동물 선택하기")

    var = IntVar()
    photo1 = PhotoImage(file = "GIF/dog.gif")
    photo2 = PhotoImage(file = "GIF/cat.gif")
    photo3 = PhotoImage(file = "GIF/rabbit.gif")

    labeltitle = Label(window, text = "좋아하는 동물 투표", font = ("궁서체", 30), fg = "blue")

    rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3)

    button1 = Button(window, text = "사진 보기", command = getphoto)

    labelImage = Label(window, width = 250, height = 250)

    labeltitle.pack(pady = 5)
    rb1.pack(pady = 5)
    rb2.pack(pady = 5)
    rb3.pack(pady = 5)
    button1.pack(pady = 5)
    labelImage.pack(pady = 5)

    window.mainloop()