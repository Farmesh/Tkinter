from tkinter import *
root = Tk()
root.geometry("444x230")
root.title("Farmesh")

# Important LAble Options
# text - Adds the Text
# bd - Background
# fg -- foreground
# font - set font   font=("comicsans",46,"bold")   font="comicsans" 46 bold"
# paddy - y padding
# paddx
# relief -- border Styling  -- SUNKEN ,RAISED,GROOVE,RIDGE

title_lable = Label(text='''khfgdhgfjhgsjhgjjsduhihgsjhgjjsduhiue
                    \n khfgdhgfjhgsjhgjjsduhiue
                    \n khfgdhgfjhgsjhgjjsduhiue
                    \n khfgdhgfjhgsjhgjjsduhiue
                    khfgdhgfjhgsjhgjjsduhiue
                     \n fdgdhgkjsdhsf''',bg="yellow",fg="red",padx=50,pady=50,font="comicsans 19 bold",borderwidth =4,relief=SUNKEN)
# Important Pack Options
# Anchor = nw , ne ... anchor="ne"
# side = top,BOTTOM,left ,RIGHT 
#Fill
#padx
#pady
title_lable.pack(side=LEFT,fill=Y,padx=34,pady=34)



root.mainloop()


