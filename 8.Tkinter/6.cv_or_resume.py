from tkinter import *

root = Tk()

Label__1=Label(root,text="Name  : ")
Label__name=Label(root,text="Vijay Rajesh R")
Label__2=Label(root,text="Age  : ")
Label__age=Label(root,text="19")
Label__3=Label(root,text="Job role  : ")
Label__role=Label(root,text="Software Developer")

Label__1.grid(row=0,column=0)
Label__2.grid(row=1,column=0)
Label__3.grid(row=2,column=0)

Label__name.grid(row=0,column=1)
Label__age.grid(row=1,column=1)
Label__role.grid(row=2,column=1)



root.mainloop()