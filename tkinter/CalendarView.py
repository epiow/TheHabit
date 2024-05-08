from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Button
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_hex

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_fake_data(start_date, end_date):
    """
    Generate fake data for the heatmap.
    """
    date_range = end_date - start_date
    num_days = date_range.days + 1
    data = np.random.rand(num_days)  # Generate random values
    num_weeks = num_days // 7
    data = data[:num_weeks*7]  # Trim excess days
    return data.reshape(num_weeks, 7)  # Reshape into weeks

def plot_calendar_heatmap(data, start_date, canvas):
    """
    Plot a calendar heatmap with horizontal cells.
    """
    data = data.T
    cmap = plt.cm.Greens  # Choose colormap
    cell_width = 20  # Width of each cell
    cell_height = 20  # Height of each cell
    for week_idx, week_data in enumerate(data):
        for day_idx, value in enumerate(week_data):
            color = cmap(value)
            alpha = value * 0.8  # Adjust the opacity here
            rgba_color = (*color[:3], alpha)
            hex_color = to_hex(rgba_color)  # Convert to hexadecimal string
            x0 = 190.0 + day_idx * cell_width  # Adjusted position
            y0 = 90.0 + week_idx * cell_height  # Adjusted position
            x1 = x0 + cell_width  # Adjusted width
            y1 = y0 + cell_height  # Adjusted height
            canvas.create_rectangle(x0, y0, x1, y1, fill=hex_color, outline="", tags="heatmap")

window = Tk()
window.geometry("800x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 187.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(393.0, 55.0, image=image_image_2)

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
data = generate_fake_data(start_date, end_date)

plot_calendar_heatmap(data, start_date, canvas)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(96.0, 242.0, image=image_image_4)

window.resizable(True, True)
window.mainloop()
