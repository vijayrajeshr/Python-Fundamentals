import tkinter as tk

def create_notepad(window):
    text_area = tk.Text(window, wrap=tk.WORD)
    text_area.pack(fill=tk.BOTH, expand=True)

window = tk.Tk()
window.title("Vijay's Notebook")

create_notepad(window)

window.mainloop()
