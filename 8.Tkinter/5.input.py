from tkinter import*

def onclick():
    given_input=input.get()
    print(given_input)

root = Tk()



input=Entry(root,width=35)
input.pack()

submit_button= Button(root,text="Submit Button",command=onclick)
submit_button.pack()

root.mainloop()