from tkinter import *
from PIL import Image,_ImageTk   #for jpg img
root = Tk()

root.geometry("1500x1500")
photo = PhotoImage(file="Farmeshkumar.png")
lable = Label(image=photo)
lable.pack()
#for jpg images

# image = Image.open(".jpg")
# photo = _ImageTk.photoImage(image)


#install PILO module
root.mainloop()