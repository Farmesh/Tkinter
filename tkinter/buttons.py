from tkinter import *
root = Tk()
root.geometry("630x400")

def hello():
    print("Hello Duniya")

f1 = Frame(root,bg="grey",borderwidth=8,relief=RIDGE)
f1.pack(side=LEFT,fill=Y)
l1 = Label(f1,text="Side Bar",bg="grey",font="comicsans 12 bold",fg="white")
l1.pack(padx=40)
f2 = Frame(root,bg="grey",borderwidth=8,relief=RIDGE)
f2.pack(fill=X)
l2 = Label(f2,text="Welome to My Project",bg="grey",font="TimesNewRoman 15 bold",fg ="white")
l2.pack()


f3 =Frame(root,bg="grey",borderwidth=8,relief=SUNKEN )
f3.pack(side=LEFT,padx=50,pady=20)

b1 = Button(f3,fg="red",text="Print",command=hello)   #calling functions
b1.pack(side=LEFT,padx=45,pady=80)
b2 = Button(f3,fg="red",text="Print")
b2.pack(side=LEFT,padx=45,pady=80)
b3 = Button(f3,fg="red",text="Print")
b3.pack(side=LEFT,padx=45,pady=80)


#button 
b1 = ()



root.mainloop()