#to create cv, give add buttuon, onclick, we have to  input infos like name, age, registration number  (Reg.no), give submit button 
import tkinter as tk

def add_info():
    name = name_entry.get()
    age = age_entry.get()
    reg_no = reg_no_entry.get()

    # You would typically save this data to a file or database here
    print(f"Name: {name}, Age: {age}, Reg. No.: {reg_no}")

root = tk.Tk()
root.title("Vijay's Task414")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

reg_no_label = tk.Label(root, text="Reg. No.:")
reg_no_label.pack()
reg_no_entry = tk.Entry(root)
reg_no_entry.pack()

add_button = tk.Button(root, text="Add", command=add_info)
add_button.pack()

root.mainloop()
