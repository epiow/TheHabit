from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from PIL import Image
import sys
import customtkinter

# Pachange nalang muna here ng link to Model
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/CPE106L/TheHabit/TheHabit/Model')
from modelClassData import Data
from modelFirebaseToPython import Firebase

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "LoginTabAssets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


user = Data()

def login():
    email = entry_1.get()
    password = entry_2.get()
    logged_in_user = user.login_user(email, password)
    if logged_in_user:
        # Login successful, perform any necessary actions
        # For example, you can open the next GUI
        open_next_gui()
    else:
        # Login failed, display an error message or handle the failure case
        print("Login failed. Please check your credentials.")

def switch_to_sign_up():
    window.destroy()
    import signUpView
    signUpView.main()

def open_next_gui():
    window.destroy()
    import MainDashboard
    MainDashboard.main(user)

def close_button():
    window.destroy()

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
#window.overrideredirect(True)  # Remove standard title bar

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

canvas = customtkinter.CTkCanvas(
    master=window,
    bg="#D9D9D9",
    height=840,
    width=633,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load images using CTkImage
image_image_1 = customtkinter.CTkImage(
    light_image=Image.open(relative_to_assets("image_1.png")),
    dark_image=Image.open(relative_to_assets("image_1.png")),
    size=(320, 533)
)
image_2 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("image_2.png")), size=(459,242))
image_3 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("image_3.png")))
entry_image_1 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("entry_1.png")))
entry_image_2 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("entry_2.png")))
button_image_1 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("button_1.png")))
button_image_2 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("button_2.png")))
button_image_3 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("image_5.png")))
image_4 = customtkinter.CTkImage(light_image=Image.open(relative_to_assets("image_4.png")))


# Create entries
entry_1 = customtkinter.CTkEntry(
    master=canvas,
    width=477,
    height=52,
    bg_color="#FFFFFF",
    fg_color="#000716",
    text_color="#000716",
    border_width=0,
    corner_radius=0,
    font=("Rockwell", 26)
)
entry_1.place(x=82.0, y=451.0)

entry_2 = customtkinter.CTkEntry(
    master=canvas,
    width=477,
    height=56,
    bg_color="#FFFFFF",
    fg_color="#000716",
    text_color="#000716",
    border_width=0,
    corner_radius=0,
    font=("Rockwell", 26)
)
entry_2.place(x=82.0, y=561.0)

# Create buttons
button_1 = customtkinter.CTkButton(
    master=canvas,
    image=button_image_1,
    text="",
    fg_color="transparent",
    border_width=0,
    hover_color="#B9B9B9",
    command=login,
    width=304.34857177734375,
    height=56.1619873046875
)
button_1.place(x=166.0, y=648.0)

button_2 = customtkinter.CTkButton(
    master=canvas,
    image=button_image_2,
    text="",
    fg_color="transparent",
    border_width=0,
    hover_color="#B9B9B9",
    command=switch_to_sign_up,
    width=304.34857177734375,
    height=56.1619873046875
)
button_2.place(x=166.0, y=733.0)

button_3 = customtkinter.CTkButton(
    master=canvas,
    image=button_image_3,
    text="",
    fg_color="transparent",
    border_width=0,
    hover_color="#B9B9B9",
    command=close_button,
    width=25,
    height=25
)
button_3.place(x=595.0, y=15.0)

window.resizable(False, False)
window.mainloop()