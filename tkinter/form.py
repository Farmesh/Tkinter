from tkinter import *
root = Tk()
root.geometry("655x400")

#Heading
Label(root,text="Welcome To RDJ", font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

#text for our form
name = Label(root,text="Name")
phone = Label(root,text = "Phone no.")
Gender = Label(root,text = "Gender")
Course = Label(root,text = "Course")
Sem = Label(root,text = "Semester")
pay_md = Label(root,text = "Payment Mode")

#pack text
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
Course.grid(row=4,column=2)
Sem.grid(row=5,column=2)
pay_md.grid(row=6,column=2)

#tkinter variables for storing entries
name_val =StringVar()
phone_val = StringVar()
Gender_val = StringVar()
Course_val = StringVar()
Sem_val = StringVar()
pay_md_val = StringVar()
Hostel = IntVar()


#Entries for our form
entry = Entry(root, textvariable=name_val)
phoneEntry = Entry(root, textvariable=phone_val)
GenderEntry = Entry(root, textvariable=Gender_val)
CourseEntry = Entry(root, textvariable=Course_val)
SemEntry = Entry(root, textvariable=Sem_val)
pay_mdEntry = Entry(root, textvariable=pay_md_val)


#packing entries
entry.grid(row = 1 ,column = 3)
phoneEntry.grid(row =2 ,column = 3)
GenderEntry.grid(row =3 ,column = 3)
CourseEntry.grid(row = 4,column = 3)
SemEntry.grid(row = 5,column = 3)
pay_mdEntry.grid(row =6 ,column = 3)

#Check Box
# Hostel = Checkbutton(text="want Hostel", variable=hostel_val)
# Hostel.grid(row = 7 , column=3)


root.mainloop()