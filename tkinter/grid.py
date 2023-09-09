from tkinter import *
root = Tk()
root.geometry("666x400")


def getvals():
    print(uservalue.get())
    print(passval.get())
user = Label(root, text= "username")
password = Label(root, text= "Password")
user.grid() #packing method
password.grid(row=1)

#variable classes in tkinter
# DoubleVar,IntVar,CHAR,BooleanVar,StringVar
#entry widget ---  takes input
uservalue = StringVar()
passval = StringVar()


userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passval)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid(row=1,column=2)

root.mainloop()