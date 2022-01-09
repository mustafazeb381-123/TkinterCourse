from tkinter import *
root = Tk()
root.title("It's ZEbU Notepad")
root.geometry("700x400")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
f2 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l = Label(f1, text="Project Tkinter Pycharm")
l.pack(pady=142)
l = Label(f2, text="Welcome To Notepad", font="Helvetica 16 bold", fg="red")
l.pack(pady=25)

root.mainloop()