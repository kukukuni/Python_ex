# gui01.py
# Python GUI --> tkinter, wxPython,PyQt
# 위젯 (Button,Label,Entry,,,,)
from tkinter import *

def btn1Click():
    text1.insert(0,text1.get()+"님 어서오세요")

window = Tk()  #tkinter에서는 Tk가 생성자가 되는 것임
#################
label1  = Label(window,text="이 름")
label1.grid(row=0,column=0)
#label1.pack()

text1 = Entry(window)
text1.grid(row=0,column=1)
#text1.pack()

button1 = Button(window, bg="yellow",text="입 력",command=btn1Click)
#command=btn1Click위에서 함수로 선언해서 누를시에 생길 행동을 지시

#button1["fg"] = "yellow"
#button1["bg"] = "red"
button1.grid(row=1,column=1)
#button1.pack()

#################
window.mainloop()    #화면이 유지되게 하려면 mainloop를 해야 한다.
