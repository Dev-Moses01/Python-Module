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
    msg = messagebox.showinfo("Warning", "Do you want to calculate the denomination count?")
    if msg == "ok":
        topwin()

button = Button(window, text="Let's get started...", bg="orange", command=confirm)
button.pack()

def topwin():
    top = Toplevel()
    top.geometry("400x400")
    top.config(bg="orange")
    top.title("Denomination Calculator")

    total_amount = Label(top, text="Enter the total amount", font=("monospace", 13), bg="orange")
    total_amount.place(x=130, y=70)
    amount = Entry(top)
    amount.place(x=150, y=95)

    label = Label(top, text="Here are the number of notes for each denomination", bg="orange", font=("monospace", 10))
    label.place(x=60, y=155)
    two_thousand = Label(top, text=2000, bg="orange", font="bold")
    two_thousand.place(x=100, y=180)
    t1 = Entry(top)
    t1.place(x=150, y=180)

    five_hundred = Label(top, text=500, bg="orange", font="bold")
    five_hundred.place(x=100, y=205)
    t2 = Entry(top)
    t2.place(x=150, y=205)

    one_hundred = Label(top, text=100, bg="orange", font="bold")
    one_hundred.place(x=100, y=230)
    t3 = Entry(top)
    t3.place(x=150, y=230)

    def calculator():
        amt = int(amount.get())
        note2000 = amt // 2000
        amt %= 2000
        note500 = amt // 500
        amt %= 500
        note100 = amt // 100
        
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))

    calculate = Button(top, text="calculate", bg="gold", font=("serif", 13), command=calculator)
    calculate.place(x=175,y=120)

window.mainloop()