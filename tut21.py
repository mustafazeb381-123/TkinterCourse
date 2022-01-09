from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i=0
root = Tk()
root.geometry("700x400")
root.title("ListBox tut")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text="Add item", command=add).pack()

root.mainloop()