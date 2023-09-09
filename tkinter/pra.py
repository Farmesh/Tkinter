from tkinter import *
root = Tk()
root.geometry("650x400")


#functions 
def btn1():
    print("Btn 1 Pressed")
def btn2():
    print("Btn 2 Pressed")
def btn3():
    print("Btn 3 Pressed")
def btn4():
    print("Btn 4 Pressed")
f1 = Frame(root,bg="grey",borderwidth=8,relief=GROOVE)
f1.pack(side=LEFT,anchor=NW)

b1 = Button(f1,bg="Black",fg="White",text="press Here",command=btn1)
b1.pack(side=LEFT,padx=60,pady=70)

b2= Button(f1,bg="Black",fg="White",text="btn2",command=btn2)
b2.pack(side=LEFT,padx=60,pady=70)

b3 = Button(f1,bg="Black",fg="White",text="btn3",command=btn3)
b3.pack(side=LEFT,padx=60,pady=70)

b4 = Button(f1,bg="Black",fg="White",text="btn4",command=btn4)
b4.pack(side=LEFT,padx=60,pady=70)
root.mainloop()