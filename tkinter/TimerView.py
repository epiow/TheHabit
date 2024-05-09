from pathlib import Path
import time
from tkinter import Tk, Label, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "TimerAssets"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("633x840")
window.configure(bg = "#FFFFFF")
window.overrideredirect(True)  # Remove standard title bar




current_time = 0
is_running = False


def update_time():
  global current_time, is_running

  if is_running:
    current_time += 0.01  # Update time every 10 milliseconds
    formatted_time = time.strftime("%M:%S", time.gmtime(current_time))  # Without microseconds
    elapsed_time_label.config(text=formatted_time)
    window.after(10, update_time)  # Schedule next update after 10 milliseconds

def start_stop():
  global is_running
  if not is_running:
    is_running = True
    update_time()
  else:
    is_running = False

def reset():
  global current_time, is_running
  current_time = 0
  is_running = False
  elapsed_time_label.config(text="00:00")


# Calculate window position for centering
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 633
window_height = 840
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 840,
    width = 633,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Remove the creation of the elapsed_time_label from the window
elapsed_time_label = Label(window, text="00:00", font=("Rockwell", 75), background="#1D2833", foreground="#FFFFFF")

# Place the label on top of image_3.png
canvas.create_window(318.0, 389.0, window=elapsed_time_label, anchor='center')


canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    633.0,
    840.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=82.0,
    y=756.0,
    width=200.0,
    height=56.1619873046875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start_stop,
    relief="flat"
)
button_2.place(
    x=82.0,
    y=670.0,
    width=200.0,
    height=56.1619873046875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=start_stop,
    relief="flat"
)
button_3.place(
    x=357.0,
    y=756.0,
    width=200.0,
    height=56.1619873046875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=357.0,
    y=670.0,
    width=200.0,
    height=56.1619873046875
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    129.0,
    78.0,
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
    318.0,
    389.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
