from tkinter import*

root= Tk()

def on__click():
    disp__label= Label(root,text="The button was clicked!!")
    disp__label.pack()

Button_1=Button(root,text="button",command=on__click)
Button_1.pack()

root.mainloop()