from tkinter import *
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("500x600")
window.configure(bg="white")

upload = Image.open("Desktop.jpg")
rock = ImageTk.PhotoImage(upload)
up = Image.open("Logo1.jpg")
paper = ImageTk.PhotoImage(up)
uplo = Image.open("Logo2.jpg")
scissors = ImageTk.PhotoImage(uplo)

image_list = [rock, paper, scissors]
pick_random = randint(0,2)
image_label = Label(window, image=image_list[pick_random], height=250, width=250)
image_label.pack(pady=20)

def spin():
    pick_random = randint(0,2)
    image_label.config(image=image_list[pick_random])

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_random == 0:
            win_lose_label.config(text="It's A Tie!! Spin Again....")
        elif pick_random == 1:
            win_lose_label.config(text="Paper Covers Rock!! You Lose....")
        elif pick_random == 2:
            win_lose_label.config(text="Rock Smashes Scissors!! You Win....")

    if user_choice_value == 1:
        if pick_random == 0:
            win_lose_label.config(text="Paper Covers Rock!! You Win....")
        elif pick_random == 1:
            win_lose_label.config(text="It's A Tie!! Spin Again....")
        elif pick_random == 2:
            win_lose_label.config(text="Scissors Cuts Paper!! You Lose....")

    if user_choice_value == 2:
        if pick_random == 0:
            win_lose_label.config(text="Rock Smashes Scissors!! You Lose....")
        elif pick_random == 1:
            win_lose_label.config(text="Scissors Cuts Paper!! You Win....")
        elif pick_random == 2:
            win_lose_label.config(text="It's A Tie!! Spin Again....")        



user_choice = ttk.Combobox(window, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)

spin_button = Button(window, text="Spin!!", command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(window, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)
window.mainloop()