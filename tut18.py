from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Pycharm")
root.geometry("700x500")

def myfunc():
    print("It's done")

def help():
    print("i will help you")
    tmsg.showinfo("Help", "I will help you with this GUI")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "you used this GUI.... was your experience Good?")
    print(value)
    if value == "yes":
        msg = "Great. please rate us on appstore"
    else:
        msg = "Tell me what went wrong, we will call you soon"
    tmsg.showinfo("Experience", msg)
def Mahnoor():
    ans = tmsg.askretrycancel("Mahnoor sa dosti kar lo", "ka di bara okatal no stargi ba mi darna obasali v")
    if ans:
        print("try kolo bandi sa zeee kho na rasha za ba hum try okaam")
    else:
        print("Shukur da chi bach shoom geni stargi ba rana obasali v laka da Said ull Ameen")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Past", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Befriend Mahnoor", command=Mahnoor)
m3.add_command(label="Rate us", command=rate)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
root.mainloop()