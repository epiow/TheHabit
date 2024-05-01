from Model.modelClassEntry import *
class Calendar:
    def __init__(self):
        self.current_year: int = 0
        self.years: list[Year]= []
class Year:
    def __init__(self, value):
        self.value = value
        self.current_month = 0
        self.months: list[Month] = []

    def addMonth(self, value):
        monthToIncrement = self.findMonth(value)
        if monthToIncrement == None:
            new_month = Year(value)
            self.months.append(new_month)
            return True
        else:
            return False
    
    def findMonth(self, value):
        for month in self.months:
            if month.value == value:
                return self.months.index(value)
        return None
    
    def setCurrentMonth(self, value):
        monthToSet = self.findMonth(value)
        if monthToSet != None:
            self.current_month = monthToSet
            return self.months[self.current_month]
        return None
    
    def editMonth(self, value):
        valueSet = False
        if not self.findMonth(value):
            if value != None:
                valueSet = True
                self.months[self.current_month].value = value
        return valueSet
    def deleteMonth(self):
        del self.months[self.current_month]
        self.current_month = None
        
class Month:
    def __init__(self, value):
        self.value = value
        self.current_week = 0
        self.weeks: list[Day] = []
    def addWeek(self, value):
        weekToIncrement = self.findWeeks(value)
        if weekToIncrement == None:
            new_month = Year(value)
            self.months.append(new_month)
            return True
        else:
            return False
    
    def findWeek(self, value):
        for month in self.months:
            if month.value == value:
                return self.months.index(value)
        return None
    
    def setCurrentMonth(self, value):
        monthToSet = self.findWeek(value)
        if monthToSet != None:
            self.current_month = monthToSet
            return self.months[self.current_month]
        return None
    
    def editMonth(self, value):
        valueSet = False
        if not self.findWeek(value):
            if value != None:
                valueSet = True
                self.months[self.current_month].value = value
        return valueSet
    def deleteMonth(self):
        del self.months[self.current_month]
        self.current_month = None
        
class Day:
    def __init__(self, value):
        self.value = value
        self.current_activity = 0
        self.activities: list[Entry] = []
