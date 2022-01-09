from tkinter import *
root = Tk()
root.geometry("700x400")
def hello():
    print("hello it's your tkinter project")

def name():
    print("i m mustafa zeb")

frame = Frame(root, borderwidth=6, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
b1 = Button(frame, fg="red", text="hey", command=hello)
b1.pack(side=LEFT, padx=23)
b2 = Button(frame, fg="red", text="tell me name now", command=name)
b2.pack(side=LEFT, padx=23)
b3 = Button(frame, fg="red", text="print now")
b3.pack(side=LEFT, padx=23)
b4 = Button(frame, fg="red", text="print now")
b4.pack(side=LEFT, padx=23)
root.mainloop()