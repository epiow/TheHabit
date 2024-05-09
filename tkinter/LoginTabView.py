from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Button
from datetime import datetime, timedelta, date
import numpy as np
import matplotlib.colors as colors
from matplotlib.colors import to_hex

# Function to convert relative path to absolute path in assets directory
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets" / "MainDashboardAssets"
    return ASSETS_PATH / Path(path)

def custom_heatmap_colormap():
    """
    Create a custom colormap with #1BCF6E as the maximum value.
    """
    cmap = colors.LinearSegmentedColormap.from_list(
        "custom_heatmap",
        [(0.0, "#FFFFFF"), (1.0, "#1BCF6E")],  # Color range (white to #1BCF6E)
    )
    return cmap

def generate_fake_data(start_date, end_date):
    """
    Generate fake data for the heatmap.
    """
    date_range = end_date - start_date
    num_days = date_range.days + 1
    data = np.random.rand(num_days) # Generate random values
    num_weeks = num_days // 7
    data = data[:num_weeks*7]  # Trim excess days
    return data.reshape(num_weeks, 7)  # Reshape into weeks

def plot_calendar_heatmap(data, start_date, canvas):
    """
    Plot a calendar heatmap with horizontal cells.
    """
    data = data.T
    cmap = custom_heatmap_colormap()  # Choose colormap
    cell_width = 20  # Original cell width
    cell_height = 20  # Original cell height
    # Increase spacing between cells (adjust as needed)
    cell_spacing_x = 10  # Additional horizontal spacing
    cell_spacing_y = 8   # Additional vertical spacing

    for week_idx, week_data in enumerate(data):
        for day_idx, value in enumerate(week_data):
            color = cmap(value)
            alpha = value * 0.5  # Adjust the opacity here
            rgba_color = (*color[:3], alpha)
            hex_color = to_hex(rgba_color)  # Convert to hexadecimal string

            # Adjust x and y coordinates with cell spacing
            x0 = 190.0 + day_idx * (cell_width + cell_spacing_x) - 35
            y0 = 90.0 + week_idx * (cell_height + cell_spacing_y) + 125
            x1 = x0 + cell_width # Adjusted width
            y1 = y0 + cell_height  # Adjusted height
            canvas.create_rectangle(x0, y0, x1, y1, fill=hex_color, outline="", tags="heatmap")

def close_button():
    window.destroy()

# Create main window
window = Tk()
window.geometry("1231x840")
window.configure(bg="#FFFFFF")
window.overrideredirect(True)

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate window position for centering
window_width = 1231
window_height = 840
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

# Set window geometry and position
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
window.configure(bg="#FFFFFF")

# Create canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=840,
    width=1231,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Place images and buttons on canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(615.0, 420.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(253.0, 690.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(695.0, 423.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(133.0, 310.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(187.0, 68.0, image=image_image_5)

canvas.create_rectangle(167.0, 210.0, 1222.0, 406.0, fill="#FFFFFF", outline="")
canvas.create_rectangle(4.0, 0.0, 79.0, 840.0, fill="#D9D9D9", outline="")

# Create buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=1242.0, y=15.0, width=25.0, height=25.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place(x=11.0, y=16.0, width=45.0, height=45.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
button_3.place(x=11.0, y=71.0, width=45.0, height=45.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=close_button, relief="flat")
button_4.place(x=1194.0, y=12.0, width=25.0, height=25.0)

# Generate and plot calendar heatmap
today = date.today()
start_date = today - timedelta(days=30)
end_date = today + timedelta(days=335)
data = generate_fake_data(start_date, end_date)
plot_calendar_heatmap(data, start_date, canvas)

window.resizable(False, False)
window.mainloop()
