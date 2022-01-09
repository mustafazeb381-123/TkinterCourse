from tkinter import *

def Zebu(event):
    print(f"you clicked on the button at {event.x} {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x344")

widget = Button(root, text="Clicked me please")
widget.pack()

widget.bind('<Button-1>', Zebu)
widget.bind('<Double-1>', quit)

root.mainloop()