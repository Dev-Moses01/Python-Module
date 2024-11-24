from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.configure(bg="yellow")
window.geometry("500x500")

upload = Image.open("app_img.jpg")
cash_tally = ImageTk.PhotoImage(upload)

label = Label(window, image=cash_tally)
label.pack()

welcome = Label(window, text="Hey User!! Welcome to the denomination calculator", bg="yellow", font="monospace")
welcome.pack()

def confirm():
    messagebox.showinfo("Warning", "Do you want to calculate the denomination count?")

button = Button(window, text="Let's get started...", bg="orange", command=confirm)
button.pack()
window.mainloop()