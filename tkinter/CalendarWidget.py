import tkinter as tk
import calendar
import datetime
import tkinter.simpledialog as sd




class CalendarApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  # Save the parent widget (the canvas)

        self.month = tk.IntVar()
        self.year = tk.IntVar()

        # Get the current month and year
        today = datetime.date.today()
        self.month.set(today.month)
        self.year.set(today.year)

        self.create_widgets()
        self.show_calendar()  # Show the current month calendar upon opening

    def create_widgets(self):
        self.header = tk.Label(self, text="Calendar", font=("Arial", 18))
        self.header.grid(row=0, column=1, pady=10)

        self.month_label = tk.Label(self, text="Month:")
        self.month_label.grid(row=1, column=0)

        self.month_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.month, width=5)
        self.month_spinbox.grid(row=1, column=1)

        self.year_label = tk.Label(self, text="Year:")
        self.year_label.grid(row=1, column=2)

        self.year_spinbox = tk.Spinbox(self, from_=1900, to=2100, textvariable=self.year, width=8)
        self.year_spinbox.grid(row=1, column=3)

        self.show_button = tk.Button(self, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=1, column=4)

        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.grid(row=2, column=0, columnspan=5, padx=20, pady=10)



    def show_calendar(self):
        self.calendar_frame.destroy()
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.grid(row=2, column=0, columnspan=5, padx=20, pady=10)

        year = self.year.get()
        month = self.month.get()
        cal = calendar.monthcalendar(year, month)

        # Get the current date
        today = datetime.date.today()

        for row_num, week in enumerate(cal):
            for col_num, day in enumerate(week):
                if day != 0:
                    button = tk.Button(self.calendar_frame, text=str(day), width=4, height=2, command=lambda d=day: self.on_date_click(d))
                    
                    # Check if the current day matches the selected date
                    if year == today.year and month == today.month and day == today.day:
                        button.config(bg="#0D8E49")  # Highlight current date with a different color
                    else:
                        button.config(bg="#1BCF6E")  # Default color for other dates
                    
                    button.grid(row=row_num, column=col_num, padx=3, pady=3)
                    button.config(relief=tk.RIDGE, borderwidth=2, font=("Arial", 12), cursor="hand2")

                    date_str = f"{year}-{month:02d}-{day:02d}"
                    note = self.get_note_for_date(date_str)
                    if note:
                        tk.Label(self.calendar_frame, text=note, fg="blue").grid(row=row_num, column=col_num, padx=3, pady=3)
                else:
                    tk.Label(self.calendar_frame, text="").grid(row=row_num, column=col_num, padx=3, pady=3)

    def on_date_click(self, day):
        selected_date = f"{self.year.get()}-{self.month.get():02d}-{day:02d}"
        print("Selected date:", selected_date)

    def on_date_click(self, day):
        selected_date = f"{self.year.get()}-{self.month.get():02d}-{day:02d}"
        print("Selected date:", selected_date)
        note = self.get_note_for_date(selected_date)
        user_note = sd.askstring("Note for Date", f"Enter note for {selected_date}:", initialvalue=note)
        if user_note is not None:
            self.save_note_for_date(selected_date, user_note)

    def get_note_for_date(self, date):
        # In a real application, this method would retrieve the note from a database or file
        # For demonstration purposes, let's assume we have a dictionary storing notes
        notes = {
        }
        return notes.get(date, "")

    def save_note_for_date(self, date, note):
        # In a real application, this method would save the note to a database or file
        # For demonstration purposes, let's just print the note
        print(f"Note for {date} saved: {note}")