from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Slider")
root.geometry("700x400")

def getdollar():
    print(f"we have credited, {myslider2.get()} dollar to your account")
    tmsg.showinfo("Amount Credited!", f"we have credited {myslider2.get()} dollar to your bank account")

Label(root, text="how much dollar do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.pack()
Button(root, text="Get Dollar!", pady=10, command=getdollar).pack()

root.mainloop()