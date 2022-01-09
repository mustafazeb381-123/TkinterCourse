from tkinter import *
def getvals():
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
root = Tk()
root.geometry("700x400")
root.title("First GUI of tkinter in python")
user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid(row=1)
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()
root.mainloop()
