from modelClassEntry import Entry
import numpy as np
class Activity():
    def __init__(self, activity_name):
        self.activity_name: str = activity_name
        self.currentEntry: int = None
        self.entries: list[Entry] = []

    def createEntry(self, date_performed, time_set, time_elapsed, count, notes=""):
        entryToIncrement = self.findEntry(date_performed)
        if entryToIncrement == None:
            new_entry = Entry(date_performed, time_set, time_elapsed, count, notes)
            self.entries.append(new_entry)
            return True
        elif self.entries[entryToIncrement].time_set == time_set:
            self.entries[entryToIncrement].count += 1
            return True
        return False
    def calculateHeatmap(self):
        heatmap_data = []
        dates: list[list[int]] = []
        for entry in self.entries:
            year, month, date = entry.date_performed.split("-")
            dates.append([int(year), int(month), int(date)])
        dates = [min(dates), max(dates)]
        day = 1
        i = 0
        while i < len(self.entries):
            entry = self.entries[i]
            if(int(entry.date_performed.split("-")[2]) == day):
                heatmap_data.append(entry.count)
            else:
                heatmap_data.append(0)
                i -= 1
            if(day == dates[1]): break
            day += 1
            i += 1

        heatmap_data = np.array(heatmap_data)
        heatmap_data = (heatmap_data + 0.5 - np.min(heatmap_data)) / (np.max(heatmap_data) + 0.5 - np.min(heatmap_data))
        print(self.activity_name, heatmap_data)
        return heatmap_data
    def calculateStreak(self):
        streaks = []
        dates: list[list[int]] = []
        for entry in self.entries:
            year, month, date = entry.date_performed.split("-")
            dates.append([int(year), int(month), int(date)])
        dates = [min(dates), max(dates)]
        day = 1
        count = 0
        for entry in self.entries:
            if(int(entry.date_performed.split("-")[2]) == day):
                count += 1
            else:
                streaks.append(count)
                count = 0
            day += 1
        return streaks
    def getCurrentEntryNotes(self):
        return self.entries[self.currentEntry].notes
    def findEntry(self, date_performed):
        for entry in self.entries:
            if entry.date_performed == date_performed:
                return self.entries.index(entry)
        return None
    
    def setCurrentEntry(self, date_performed):
        entryToSet = self.findEntry(date_performed)
        if entryToSet != None:
            self.currentEntry = entryToSet
            return self.entries[self.currentEntry]
        return None
    
    def editEntry(self, date_performed=None, time_set=None, time_elapsed=None, count=None, notes=None):
        dateSet = False
        timeSet = False
        elapsedSet = False
        countSet = False
        notesSet = False
        if not self.findEntry(date_performed):
            if date_performed != None:
                dateSet = True
                self.entries[self.currentEntry].date_performed = date_performed
            if time_set != None:
                timeSet = True
                self.entries[self.currentEntry].time_set = time_set
            if time_elapsed != None:
                elapsedSet = True
                self.entries[self.currentEntry].time_elapsed = time_elapsed
            if count != None:
                countSet = True
                self.entries[self.currentEntry].count = count
            if notes != None:
                notesSet = True
                self.entries[self.currentEntry].notes = notes
        return [dateSet, timeSet, elapsedSet, countSet, notesSet]
                
    def deleteEnty(self):
        del self.entries[self.currentEntry]
        self.currentEntry = None
        