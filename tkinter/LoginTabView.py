from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import sys
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/C++/CPE106L/TheHabit/TheHabit/Model')

from modelFirebaseToPython import Firebase

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login():
    email = entry_1.get()
    password = entry_2.get()
    user = firebase.login_user(email, password)
    if user:
        # Login successful, perform any necessary actions
        # For example, you can open the next GUI
        open_next_gui()
    else:
        # Login failed, display an error message or handle the failure case
        print("Login failed. Please check your credentials.")

def open_next_gui():
    window.destroy()  # Close the current window
    import CalendarView  # Import the next GUI script
    CalendarView.main()  # Call a func

firebase = Firebase()

window = Tk()
window.geometry("327x394")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    0.0,
    327.0,
    394.0,
    fill="#D9D9D9",
    outline=""
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    167.0,
    192.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    167.0,
    246.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    167.0,
    219.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=28.0,
    y=206.0,
    width=278.0,
    height=25.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    167.0,
    273.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=28.0,
    y=260.0,
    width=278.0,
    height=25.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,  # Call the login function when button is clicked
    relief="flat"
)
button_1.place(
    x=78.3223876953125,
    y=313.96875,
    width=177.3771514892578,
    height=27.087499618530273
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    167.0,
    110.0,
    image=image_image_3
)

window.resizable(False, False)
window.mainloop()
