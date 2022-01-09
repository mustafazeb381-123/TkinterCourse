from tkinter import*
root = Tk()
root.geometry("700x400")
root.title("Scrollbar tut")
# for scrollbar to connecting to widget
# 1 = widget(yscrollcommand = scrollbar.get)
# 2 = scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(300):
    listbox.insert(END, f"item {i}")

listbox.pack(fill="both", padx=22)
scrollbar.config(command=listbox.yview)



root.mainloop()