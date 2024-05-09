from tkinter import Tk, Canvas, Button, Label
import time

window = Tk()
window.title("Stopwatch")
window.geometry("400x400")  # Adjust window size as needed

# Create a canvas for drawing the stopwatch circle
canvas = Canvas(window, width=400, height=400, bg="#FFFFFF")
canvas.pack()

center_x = 200
center_y = 200
radius = 150  # Adjust radius for circle size

# Outline circle
canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   width=5, outline="#000000")

# Inner circle for better visualization
inner_radius = radius - 20
canvas.create_oval(center_x - inner_radius, center_y - inner_radius,
                   center_x + inner_radius, center_y + inner_radius,
                   fill="#FFFFFF")

elapsed_time_label = Label(window, text="00:00", font=("Rockwell", 30), bg="#FFFFFF")
elapsed_time_label.place(relx=0.5, rely=0.5,)

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

start_button = Button(window, text="Start", command=start_stop, font=("Arial", 16))
start_button.place(relx=0.3, rely=0.8,)

reset_button = Button(window, text="Reset", command=reset, font=("Arial", 16))
reset_button.place(relx=0.7, rely=0.8,)

window.mainloop()