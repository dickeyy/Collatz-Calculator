from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import time 
import random as r

window = Tk()
window.title("Collatz Calculator by Kyle Dickey")
window.geometry("569x640")
window.configure(bg="#2D283E")

canvas = Canvas(
    window,
    bg = "#2D283E",
    height = 640,
    width = 669,
    bd = 0,
    highlightthickness = 0,
    relief =  "ridge"
)
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    0.0,
    569.0,
    640.0,
    fill="#2D283E",
    outline="")

canvas.create_text(
    40,
    20.0,
    anchor="nw",
    text="Collatz Calculator",
    fill="#802BB1",
    font=("Roboto Bold", 64 * -1)
)

canvas.create_text(
    150,
    150,
    anchor="nw",
    text="Input a number",
    fill="#D1D7E0",
    font=("Roboto Bold", 36 * -1)
)

entry_1 = Entry(
    bd=2,
    bg="#2D283E",
    highlightthickness=0,
    font=("Roboto Bold", 44 * -1),
    fg="#D1D7E0",

)

entry_1.place(
    x=103.0,
    y=200.0,
    width=364.0,
    height=55.0
)

def button_1_clicked():
    num = entry_1.get()
    num = int(num)

    global runs
    runs = 0
    global start
    start = time.time()

    while True:
        runs += 1

        # If the number is even
        if (num % 2) == 0:
            num /= 2

            if num == 1:
                break
        
        # If the number is odd
        else:
            num *= 3
            num += 1

            if num == 1:
                break

    stop = time.time()
    elapsedTime = stop - start
    messagebox.showinfo("Loop Reached", f"Loop reached... \nCalculated {runs} numbers in {elapsedTime} seconds")

button_1 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat",
    text="Calculate",
    bg="#2D283E",
    fg="#802BB1",
    font=("Roboto Bold", 24 * -1)
)

button_1.place(
    x=178.0,
    y=427.0,
    width=212.0,
    height=78.0
)

window.resizable(False, False)
window.mainloop()