from tkinter import *
root = Tk()
root.geometry("655x333")
root.title("Frame")
#frame
f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2 = Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l1 = Label(f1,text="Frame ep.")
l1.pack(padx=50)

l2 = Label(f2,text="Welcome to My Sftware",font="Arial 12 bold",bg="grey",fg="red",pady=15)
l2.pack()




root.mainloop()
