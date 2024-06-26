from pathlib import Path
import time
import pyrebase
from datetime import datetime
from config import config_keys as keys
from tkinter import Tk, Label, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "TimerAssets"

def main(user, activity_name):
    global is_running, current_time, prev_elapsed_time, paused_time

    current_time = 0
    is_running = False
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    firebase = pyrebase.initialize_app(keys)
    db = firebase.database()


    window = Tk()
    window.title("TheHabit")
    window.geometry("633x840")
    window.configure(bg = "#FFFFFF")

    def close_button():
        window.destroy()

    def choose_activity():
        pass



    def update_time():
        global current_time, is_running, start_time

        if is_running:
            current_time = time.time()  # Get current time in seconds
            elapsed_time = current_time - start_time  # Calculate elapsed time

            seconds = int(elapsed_time)
            microseconds = int((elapsed_time - seconds) * 1000000)  # Convert to microseconds

            # Create a time structure tuple using seconds
            time_tuple = time.gmtime(seconds)

            # Format time without microseconds
            formatted_time = time.strftime("%M:%S", time_tuple)

            # Append microseconds to the formatted time with two decimal places
            formatted_time += f".{int(microseconds/10000):02d}"

            elapsed_time_label.config(text=formatted_time)
            window.after(10, update_time)  # Schedule next update after 10 milliseconds

    prev_elapsed_time = 0

    def start_stop():
        global is_running, start_time, prev_elapsed_time

        if not is_running:
            is_running = True
            start_time = time.time() - prev_elapsed_time  # Resume from the previous elapsed time
            update_time()
        else:
            is_running = False
            prev_elapsed_time = time.time() - start_time  # Store the elapsed time before stopping

    def reset():
        global current_time, is_running
        current_time = 0
        is_running = False
        elapsed_time_label.config(text="00:00.000000")  # Reset with milliseconds

    paused_time = None

    def pause_timer():
        global is_running, paused_time
        if is_running:
            is_running = False
            paused_time = time.time()  # Store the current time when paused
        else:
            is_running = True
            start_time += time.time() - paused_time  # Adjust start_time to account for the pause
            paused_time = None  # Reset paused_time
            update_time()

    def log_time():
        global current_time, start_time
        elapsed_time = current_time - start_time
        seconds = int(elapsed_time)
        microseconds = int((elapsed_time - seconds) * 1000000)
        formatted_time = f"{seconds}.{int(microseconds/10000):02d}"
        print(f"Logged time: {formatted_time} seconds")
        today_date = datetime.today().strftime('%Y-%m-%d')
        print(activity_name)
        print(today_date)


        #NEED TO BE FIXED! HEATMAP PLOTTING DOES NOT WORK ON SOME VALUES
        user.currentUser.setCurrentActivity(activity_name)
        user.currentUser.activities[user.currentUser.currentActivity].createEntry(today_date, round(elapsed_time), round(elapsed_time), 4, "")
        user.write_user_data()

    #    def createEntry(self, date_performed, time_set, time_elapsed, count, notes=""):
    def back_to_dashboard():
        window.destroy()
        import MainDashboard
        MainDashboard.main(user)

    def discard_time():
        global current_time, is_running
        current_time = 0
        is_running = False
        elapsed_time_label.config(text="00:00.00")

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
    elapsed_time_label = Label(window, text="00:00.00", font=("Rockwell", 75), background="#1D2833", foreground="#FFFFFF")

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
    LogButton_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=log_time,
        relief="flat"
    )
    LogButton_1.place(
        x=82.0,
        y=756.0,
        width=200.0,
        height=56.1619873046875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    StartButton_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=start_stop,
        relief="flat"
    )
    StartButton_2.place(
        x=82.0,
        y=670.0,
        width=200.0,
        height=56.1619873046875
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    DiscardButton_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=discard_time,
        relief="flat"
    )
    DiscardButton_3.place(
        x=357.0,
        y=756.0,
        width=200.0,
        height=56.1619873046875
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    PauseButton_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=pause_timer,
        relief="flat"
    )
    PauseButton_4.place(
        x=357.0,
        y=670.0,
        width=200.0,
        height=56.1619873046875
    )
    back_image = PhotoImage(file=relative_to_assets("back.png"))

    back_button = Button(
        image=back_image, 
        borderwidth=0,
        highlightthickness=0,
        command=back_to_dashboard,
        relief="flat",
        background="#D9D9D9"
    )
    back_button.place(x=15, y=12, width=53, height=32)

    button_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    CloseButton_4 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=close_button,
        background="#D9D9D9",
        relief="flat"
    )
    CloseButton_4.place(
        x=595.0,
        y=15.0,
        width=25.0,
        height=25.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        320.0,
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
