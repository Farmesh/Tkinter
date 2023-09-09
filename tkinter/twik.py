from tkinter import *
Root = Tk()

# gui logic
Root.geometry("500x500") # widht x height
Root.minsize(100,100) #width,height  (Min size)
Root.maxsize(1000,500) 
name = Label(text="Farmesh's GUI") #to show we have to pack
name.pack()
Root.mainloop()
