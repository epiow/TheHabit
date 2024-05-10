from pathlib import Path
from tkinter import Label, Tk, Canvas, PhotoImage, Button, ttk
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib.colors import to_hex
from CalendarWidget import CalendarApp
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
sys.path.append('c:/Users/FP Sangilan/Documents/Programming Projects/CPE106L/TheHabit/TheHabit/Model')
from modelClassData import Data


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "MainDashboardAssets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main(user):
    '''
    username_label = Label(
        text=f"Logged in as: {user.currentUser.email}",
        bg="#FFFFFF",
        font=("Arial", 14),
    )
    
    username_label.place(x=20, y=20)
    '''

    
    def custom_heatmap_colormap():
        """
        Create a custom colormap with #1BCF6E as the maximum value.
        """
        cmap = colors.LinearSegmentedColormap.from_list(
            "custom_heatmap",
            [(0.0, "#FFFFFF"), (1.0, "#1BCF6E")],  # Color range (white to #1BCF6E)
        )
        return cmap

    def plot_calendar_heatmap(data, start_date, canvas):
        """
        Plot a calendar heatmap with horizontal cells.
        """
        #data = data.T
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
                x0 = 200.0 + day_idx * (cell_width + cell_spacing_x) - 35
                y0 = 90.0 + week_idx * (cell_height + cell_spacing_y) + 125
                x1 = x0 + cell_width # Adjusted width
                y1 = y0 + cell_height  # Adjusted height
                canvas.create_rectangle(x0, y0, x1, y1, fill=hex_color, outline="", tags="heatmap")

    def selected_activity():
        return combobox.get()


    def switch_to_timer():
        activity = selected_activity()
        window.destroy()
        import TimerView
        TimerView.main(user, activity)
        
    def close_button():
        window.destroy()

    def logout_button_func():
        window.destroy()
        import LoginTabView
        LoginTabView.main()

    window = Tk()
    window.title("TheHabit")
    window.geometry("1231x840")
    window.configure(bg = "#FFFFFF")
    #window.overrideredirect(True)
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

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 840,
        width = 1231,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    calendar_app = CalendarApp(canvas)
    calendar_window = canvas.create_window(714, 450, anchor="nw", window=calendar_app)

    

    canvas.create_text(
        220.0,
        480.0,
        text="Choose a Habit",
        fill="#000000",
        font=("Rockwell", 15)

    )
    canvas.create_text(
        220.0,
        480.0,
        text="Choose a Habit",
        fill="#000000",
        font=("Rockwell", 15)

    )

    combobox = ttk.Combobox(
    canvas,
    values=user.get_activities_list(),  # Replace with your options
    width=20,
    font="Rockwell",
    )

    combobox.place(x=145, y=500)



    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        615.0,
        420.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        253.0,
        690.0,
        image=image_image_2
    )
    choose_activity_image = PhotoImage(
        file=relative_to_assets("choose_activity.png")
    )
    choose_activity_button = Button(
        image=choose_activity_image,
        borderwidth=0,
        highlightthickness=0,
        command=switch_to_timer,
        relief="flat"
    )
    choose_activity_button.place(
        x=400,
        y=500,
        width=239,
        height=84
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:print('test'),
        relief="flat"
    )
    button_1.place(
        x=1242.0,
        y=15.0,
        width=25.0,
        height=25.0
    )


    logout_button_image = PhotoImage(
        file=relative_to_assets("back.png"))
    logout_button = Button(
        image=logout_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=logout_button_func,
        relief="flat"
    )
    logout_button.place(
        x=15,
        y=12,
        width=53,
        height=32
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=close_button,
        relief="flat"
    )
    button_4.place(
        x=1194.0,
        y=12.0,
        width=25.0,
        height=25.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        187.0,
        68.0,
        image=image_image_5
    )

    user.print_activities_on_canvas(canvas, 100, 220)

    today = date.today()
    start_date = today - timedelta(days=5)
    end_date = today + timedelta(days=30)

    user_heatmap = user.get_heatmap_data()
    plot_calendar_heatmap(user_heatmap, start_date, canvas)

    window.resizable(False, False)
    window.mainloop()
