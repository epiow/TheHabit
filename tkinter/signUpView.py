from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import sys
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/CPE106L/TheHabit/TheHabit/Model')
from modelFirebaseToPython import Firebase

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "signUpAssets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

firebase = Firebase()


def sign_up():
    name = entry_1.get()
    email = entry_4.get()
    password = entry_2.get()
    confirm_password = entry_3.get()


    if password == confirm_password:
        if firebase.create_user(email, password):
            firebase.set_name(name)
            print('Account Created Succesfully')
        else:
            print("Error creating user.")
    else:
        print('Password does not match')

window = Tk()
window.geometry("633x840")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 840,
    width = 633,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    633.0,
    840.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    318.5,
    429.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=80.0,
    y=402.0,
    width=477.0,
    height=52.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    318.5,
    642.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=80.0,
    y=613.0,
    width=477.0,
    height=56.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    318.5,
    569.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=80.0,
    y=540.0,
    width=477.0,
    height=56.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    318.5,
    498.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=80.0,
    y=471.0,
    width=477.0,
    height=52.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up,
    relief="flat"
)
button_1.place(
    x=166.0,
    y=715.0,
    width=304.34857177734375,
    height=56.1619873046875
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    316.0,
    237.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    607.0,
    27.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    316.0,
    420.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
