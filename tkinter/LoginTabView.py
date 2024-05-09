from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import sys

# Pachange nalang muna here ng link to Model
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/CPE106L/TheHabit/TheHabit/Model')
from modelFirebaseToPython import Firebase

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "LoginTabAssets"

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

def switch_to_sign_up():
    import signUpView
    window.destroy()
    signUpView.main()

def open_next_gui():
    import MainDashboard
    window.destroy()  # Close the current window
    MainDashboard.main()  # Call a func

def close_button():
    window.destroy()

firebase = Firebase()

window = Tk()
window.overrideredirect(True)  # Remove standard title bar

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate window position for centering
window_width = 630
window_height = 840
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

# Set window geometry and position
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
window.configure(bg="#FFFFFF")
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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    320.0,
    533.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    316.0,
    420.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    320.0,
    422.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    320.5,
    478.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Rockwell", 26)
)
entry_1.place(
    x=82.0,
    y=451.0,
    width=477.0,
    height=52.0
)


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    320.5,
    590.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Rockwell", 26)
)
entry_2.place(
    x=82.0,
    y=561.0,
    width=477.0,
    height=56.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=166.0,
    y=648.0,
    width=304.34857177734375,
    height=56.1619873046875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_sign_up,
    relief="flat"
)
button_2.place(
    x=166.0,
    y=733.0,
    width=304.34857177734375,
    height=56.1619873046875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("image_5.png"))

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=close_button,
    relief="flat",
)
button_3.place(
    x = 595.0,
    y = 15.0,
    width=25,
    height=25
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    316.0,
    237.0,
    image=image_image_4
)


window.resizable(False, False)
window.mainloop()
