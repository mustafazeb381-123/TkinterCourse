# Newspaper
from tkinter import *
import os
from PIL import Image, ImageTk
path =r"C:\Users\HP\PycharmProjects\TkinterCourse\photos.jpg"
root = Tk()
root.title("Geo news")
root.geometry("900x600")

photo = ImageTk.PhotoImage(Image.open(file=path))

photo_label = Label(image=photo)
photo_label.pack()
root.mainloop()