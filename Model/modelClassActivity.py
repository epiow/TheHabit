from Model.modelClassEntry import Entry
import numpy as np
class Activity():
    def __init__(self, activity_name):
        self.activity_name: str = activity_name
        self.currentEntry: int = None
        self.entries: list[Entry] = []

    def createEntry(self, date_performed, time_set, time_elapsed, count):
        entryToIncrement = self.findEntry(date_performed)
        if entryToIncrement == None:
            new_entry = Entry(date_performed, time_set, time_elapsed, count)
            self.entries.append(new_entry)
            return True
        elif self.entries[entryToIncrement].time_set == time_set:
            self.entries[entryToIncrement].count += 1
            return True
        return False
    def calculateHeatmap(self):
        heatmap_data = []
        for entry in self.entries:
            heatmap_data.append(entry.count)
        heatmap_data = np.array(heatmap_data)
        heatmap_data = (heatmap_data + 0.5 - np.min(heatmap_data)) / (np.max(heatmap_data) + 0.5 - np.min(heatmap_data))
        print(self.activity_name, heatmap_data)
        return heatmap_data
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
    
    def editEntry(self, date_performed=None, time_set=None, time_elapsed=None, count=None):
        dateSet = False
        timeSet = False
        elapsedSet = False
        countSet = False
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
        return [dateSet, timeSet, elapsedSet, countSet]
                
    def deleteEnty(self):
        del self.entries[self.currentEntry]
        self.currentEntry = None
        