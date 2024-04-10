import flet as ft
import os
import DataIO
import Database
import json

class User():
    def __init__(self, username, password):
        self.io = DataIO.DataIO('./JSON/data.json')
        self.db = Database.Database(self.io)
        self.username = username
        self.password = password
        self.activities = []
    def setActivities(self):
        data = self.io.load_data()
        for user in data:
            if(self.username == user["username"]):
                for activity in user["activities"]:
                    activity_to_set = Activity(activity["name"], activity["times_performed"])
                    self.activities.append(activity_to_set)
                    
    def loginUser(self):
        data = self.io.load_data()
        userExists = False
        for user in data:
            if self.username == user["username"] and self.password == user["password"]:
                userExists = True
                self.setActivities()
                break
        return userExists
            
    def registerUser(self):
        return self.db.create_user(self.username, self.password)

class Activity():
    def __init__(self, activity_name, times_performed):
        self.name = activity_name
        self.entries = []
        self.setEntries(times_performed)
    def setEntries(self, times_performed):
        for entry in times_performed:
            new_entry = ActivityEntry(entry["date_performed"], entry["time_set"], entry["time_elapsed"], 0)
            self.entries.append(new_entry)
        
class ActivityEntry():
    def __init__(self, date_performed, time_set, time_elapsed, count):
        self.date_performed = date_performed
        self.time_set = time_set
        self.time_elapsed = time_elapsed
        self.count = count

user = User("yo", "yuh")
user.loginUser()
for i in user.activities:
    print(i.name)
    for j in i.entries:
        print(j.date_performed)