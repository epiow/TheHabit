from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import sys
import LoginTabView
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
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = password_entry.get()

    if password == confirm_password:
        if firebase.create_user(email, password):
            firebase.set_name(name)
            print('Account Created Successfully')
        else:
            print("Error creating user.")
    else:
        print('Password does not match')

def back_window():
    window.destroy()
    LoginTabView.main()

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

# Entry fields and placeholder labels
name_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
email_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))
password_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Rockwell", 26))

# Place entry fields and placeholder labels
name_entry.place(x=75.0, y=455.0, width=477.0, height=54.0)
email_entry.place(x=75.0, y=555.0, width=477.0, height=54.0)
password_entry.place(x=75.0, y=655.0, width=477.0, height=54.0)


# Create buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=sign_up, relief="flat")
button_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=close_button, relief="flat")
back_image = PhotoImage(file=relative_to_assets("back.png"))
back_button = Button(image=back_image, borderwidth=0, highlightthickness=0, command=back_window, relief="flat", background="#D9D9D9")

# Place buttons
button_1.place(x=166.0, y=715.0, width=304.34857177734375, height=56.1619873046875)
button_2.place(x=595.0, y=15.0, width=25, height=25)
back_button.place(x=15, y=12, width=53, height=32)

# Create images on canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(316.0, 237.0, image=image_image_1)
image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(607.0, 27.0, image=image_image_2)
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(316.0, 420.0, image=image_image_3)
name_photo = PhotoImage(file=relative_to_assets("nameLabel.png"))
name_label = canvas.create_image(115, 437, image=name_photo)

email_photo = PhotoImage(file=relative_to_assets("emailLabel.png"))
email_label = canvas.create_image(115, 532, image=email_photo)

pass_photo = PhotoImage(file=relative_to_assets("passLabel.png"))
pass_label = canvas.create_image(140, 633, image=pass_photo)


# Configure window
window.resizable(False, False)
window.mainloop()
