from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import sys

# Add the path to the model module
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/CPE106L/TheHabit/TheHabit/Model')
from modelFirebaseToPython import Firebase

# Define paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "signUpAssets"

# Function to convert relative path to absolute path in assets directory
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize Firebase
firebase = Firebase()

# Function to handle sign-up process
def sign_up():
    name = entry_1.get()
    email = entry_4.get()
    password = entry_2.get()
    confirm_password = entry_3.get()

    if password == confirm_password:
        if firebase.create_user(email, password):
            firebase.set_name(name)
            print('Account Created Successfully')
        else:
            print("Error creating user.")
    else:
        print('Password does not match')

# Function to handle typing in entry fields


# Function to close the window
def close_button():
    window.destroy()

# Create main window
window = Tk()
window.geometry("633x840")
window.configure(bg="#FFFFFF")
window.overrideredirect(True)  # Remove standard title bar

# Calculate window position for centering
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 630
window_height = 840
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=840,
    width=633,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 633.0, 840.0, fill="#D9D9D9", outline="")

# Create entry fields with placeholder labels
DEFAULT_TEXT = "Test Text"

# Functions to hide placeholder labels when entry fields receive focus
def hide_placeholder(event, label, entry):
    if entry.get() == DEFAULT_TEXT:
        label.place_forget()



# Entry fields and placeholder labels
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
placeholder_label_1 = Label(master=window, text=DEFAULT_TEXT, font=("Rockwell", 26), fg="#aaaaaa")
entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
placeholder_label_2 = Label(master=window, text=DEFAULT_TEXT, font=("Rockwell", 26), fg="#aaaaaa")
entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
placeholder_label_3 = Label(master=window, text=DEFAULT_TEXT, font=("Rockwell", 26), fg="#aaaaaa")
entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
placeholder_label_4 = Label(master=window, text=DEFAULT_TEXT, font=("Rockwell", 26), fg="#aaaaaa")



# Place entry fields and placeholder labels
entry_1.place(x=80.0, y=402.0, width=477.0, height=52.0)
entry_2.place(x=80.0, y=613.0, width=477.0, height=56.0)
entry_3.place(x=80.0, y=540.0, width=477.0, height=56.0)
entry_4.place(x=80.0, y=471.0, width=477.0, height=52.0)
placeholder_label_1.place(x=80.0, y=402.0, width=477.0, height=52.0)
placeholder_label_2.place(x=80.0, y=613.0, width=477.0, height=56.0)
placeholder_label_3.place(x=80.0, y=540.0, width=477.0, height=56.0)
placeholder_label_4.place(x=80.0, y=471.0, width=477.0, height=52.0)

# Bind focus events to hide placeholders
entry_1.bind("<FocusIn>", lambda event: hide_placeholder(event, placeholder_label_1, entry_1))
entry_2.bind("<FocusIn>", lambda event: hide_placeholder(event, placeholder_label_2, entry_2))
entry_3.bind("<FocusIn>", lambda event: hide_placeholder(event, placeholder_label_3, entry_3))
entry_4.bind("<FocusIn>", lambda event: hide_placeholder(event, placeholder_label_4, entry_4))

# Function to handle entry field click
def handle_click(event, entry, label):
    entry.focus()  # Focus on the entry field
    if entry.get() == DEFAULT_TEXT:
        label.place_forget()  # Hide the placeholder label

# Bind click events to handle entry fields
entry_1.bind("<Button-1>", lambda event: handle_click(event, entry_1, placeholder_label_1))
entry_2.bind("<Button-1>", lambda event: handle_click(event, entry_2, placeholder_label_2))
entry_3.bind("<Button-1>", lambda event: handle_click(event, entry_3, placeholder_label_3))
entry_4.bind("<Button-1>", lambda event: handle_click(event, entry_4, placeholder_label_4))



# Create buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=sign_up, relief="flat")
button_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=close_button, relief="flat")

# Place buttons
button_1.place(x=166.0, y=715.0, width=304.34857177734375, height=56.1619873046875)
button_2.place(x=595.0, y=15.0, width=25, height=25)

# Create images on canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(316.0, 237.0, image=image_image_1)
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(607.0, 27.0, image=image_image_2)
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(316.0, 420.0, image=image_image_3)

# Configure window
window.resizable(False, False)
window.mainloop()
