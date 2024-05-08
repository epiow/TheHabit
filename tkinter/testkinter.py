from tkinter import *
import modelFirebaseToPython as fb

Firebase = fb.Firebase()

window = Tk()
window.geometry("1230x840")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    width=1230,
    height=840,
)

canvas.place(x = 0, y = 0)

window.mainloop()