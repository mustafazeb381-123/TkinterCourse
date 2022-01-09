from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Xuxxaiii GUI")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the line goes from x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0)

# to create a rectangle specify parameter in this order - coors of top left and coors of bottom right.
can_widget.create_rectangle(3, 5, 700, 300)

# to create a text
can_widget.create_text(200, 200, text="Mustafa zeb")

# to create an oval shape
can_widget.create_oval(400, 200, 200, 350)

root.mainloop()