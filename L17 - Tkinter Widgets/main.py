from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
upload = Image.open("Desktop.jpg")
background = ImageTk.PhotoImage(upload)
show = Label(window, image = background, height=500, width=500)
show.pack()

def message():
    # messagebox.showinfo("Show Information", "Start the game")
    # messagebox.showwarning("Running", "You have started the game")
    messagebox.askyesno("Confirmation", "Are you sure you want to quit")
button = Button(window, text = "Click me!!!", bg="brown", command=message)
button.pack()
window.mainloop()