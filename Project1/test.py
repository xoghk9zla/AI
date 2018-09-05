from tkinter import *

def process():
    print("한국 산업 기술 대학교")


window = Tk()
button = Button(window, text="클릭!", command=process)
button.pack()
button.place(x=240, y=110)
window.geometry("505x500")
window.mainloop()