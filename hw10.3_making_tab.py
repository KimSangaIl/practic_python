## 2019038041 김상일 ##
from tkinter import *
from tkinter import ttk

## Main Code ##
window = Tk()

maintab = ttk.Notebook(window)
dogtab = ttk.Frame(maintab)
maintab.add(dogtab, text = "강아지")
cattab = ttk.Frame(maintab)
maintab.add(cattab, text = "고양이")

dogphoto = PhotoImage(file = "gif/dog10.gif")
doglabel = Label(dogtab, image = dogphoto)
catphoto = PhotoImage(file = "gif/cat11.gif")
catlabel = Label(cattab, image = catphoto)

maintab.pack(expand = 1, fill = "both")
doglabel.pack()
catlabel.pack()

window.mainloop()