from .modelClassCalendar import *
class Entry:
    def __init__(self, date_performed, time_set, time_elapsed, count, notes=""):
        self.date_performed: str = date_performed
        self.time_set: int = time_set
        self.time_elapsed: int = time_elapsed
        self.count: int = count
        self.notes: str = notes


# retrieve notes for a specific date/activity
# read notes
