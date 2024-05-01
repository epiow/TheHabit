from Model.modelClassEntry import *
class Calendar:
    def __init__(self):
        self.current_year: int = 0
        self.years: list[Year]= []
class Year:
    def __init__(self):
        self.current_month = 0
        self.months: list[Month] = []
class Month:
    def __init__(self):
        self.current_week = 0
        self.weeks: list[Day] = []
class Day:
    def __init__(self):
        self.current_entry = 0
        self.Entries: list[Entry] = []


