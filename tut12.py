from tkinter import *
root = Tk()
def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")
    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")
root.geometry("700x400")
Label(root, text="Welcome to Xuxxaiii Co", font="comicsansms 13 bold", pady=13).grid(row=0, column=3)

# Text fro our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

# Pack text fro our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for string entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our forms
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox
foodservice = Checkbutton(text="want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button and packing it and assigning it a command
Button(text="Submit the form", command=getvals).grid(row=7, column=3)
root.mainloop()