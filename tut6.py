from tkinter import *
root = Tk()
root.title("It's Xuxaiii GUI")
root.geometry()
just_paragraph = Label(text='''my name is mustafa zeb and i m a student at UOS. and i m studying computer sciene. i love pythom 
because it's easy to learn and it's syntax is easy than other languages like java, c++, c  and c#. 
and my friend are good at java and other languages so they can making project in other langueges 
and i my self make a project in python.''', bg="red", fg="white", padx=100, pady=90, font="cosmicsansms 19 bold",
                       borderwidth=3, relief=SUNKEN)
just_paragraph.pack()
# just_paragraph.pack(side=BOTTOM, anchor="nw")# ne is north east and you can write like nw etc.
just_paragraph.pack(side=LEFT, fill=Y, padx=34, pady=34)
root.mainloop()