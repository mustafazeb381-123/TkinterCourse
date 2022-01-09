from tkinter import *
import tkinter.messagebox as tmsg
root =Tk()
root.geometry("700x400")
root.title("RadioButton tut")

def order():
    tmsg.showinfo("Order Received!", f"we have received your order for {var.get()}. Thanks for ordering")

var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Pizza", padx=14, variable=var, value="Pizza").pack(anchor="w")
radio = Radiobutton(root, text="Biryani", padx=14, variable=var, value="Biryani").pack(anchor="w")
radio = Radiobutton(root, text="Sandwich", padx=14, variable=var, value="Sandwich").pack(anchor="w")
radio = Radiobutton(root, text="Chicken", padx=14, variable=var, value="Chicken").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root.mainloop()