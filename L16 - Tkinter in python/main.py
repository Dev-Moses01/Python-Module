from tkinter import *
window = Tk()
window.geometry("500x500")
window.config(bg = "orange")
window.title("My first try on TK!!!")
#label widget
text1 = Label(window, text = "My first game", bg = "orange", fg = "aqua", font=("cursive", 15))
text1.pack()
#button widget
def onclk():
    print("You have started the game")
click = Button(window, text = "Start Game!!!", fg = "red", command = onclk)
click.pack()


window.mainloop()
