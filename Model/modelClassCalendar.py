from Model.modelClassActivity import *
class Calendar:
    def __init__(self):
        self.current_year = 0
        self.years: list[Month]= []
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
        self.current_activity = 0
        self.activities: list[Activity] = []


